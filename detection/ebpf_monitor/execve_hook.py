#!/usr/bin/env python3
# Educational eBPF Monitor using BCC (BPF Compiler Collection)
# This monitors all new process executions (execve) system-wide.
# Requires root and Linux kernel headers.

from bcc import BPF

bpf_text = """
#include <uapi/linux/ptrace.h>
#include <linux/sched.h>

// Struct to pass event data to userspace
struct data_t {
    u32 pid;
    char comm[TASK_COMM_LEN];
    char filename[256];
};

BPF_PERF_OUTPUT(events);

// Hooking the execve syscall
int syscall__execve(struct pt_regs *ctx, const char __user *filename) {
    struct data_t data = {};
    data.pid = bpf_get_current_pid_tgid() >> 32;
    bpf_get_current_comm(&data.comm, sizeof(data.comm));
    bpf_probe_read_user_str(&data.filename, sizeof(data.filename), filename);
    
    events.perf_submit(ctx, &data, sizeof(data));
    return 0;
}
"""

print("Loading eBPF program to monitor 'execve' syscalls... (Press Ctrl+C to stop)")
try:
    b = BPF(text=bpf_text)
    execve_fnname = b.get_syscall_fnname("execve")
    b.attach_kprobe(event=execve_fnname, fn_name="syscall__execve")

    print(f"{'PID':<8} {'COMMAND':<16} {'TARGET FILENAME'}")

    def print_event(cpu, data, size):
        event = b["events"].event(data)
        print(f"{event.pid:<8} {event.comm.decode('utf-8', 'replace'):<16} {event.filename.decode('utf-8', 'replace')}")

    b["events"].open_perf_buffer(print_event)
    while True:
        try:
            b.perf_buffer_poll()
        except KeyboardInterrupt:
            exit()
except Exception as e:
    print(f"eBPF initialization failed (Ensure you are root on Linux): {e}")
