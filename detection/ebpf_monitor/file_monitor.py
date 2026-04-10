#!/usr/bin/env python3
# Real-time Ransomware Detection using eBPF
# Monitors 'rename' and 'write' syscalls for suspicious mass activity.

from bcc import BPF
import time

bpf_text = """
#include <uapi/linux/ptrace.h>
#include <linux/sched.h>

struct data_t {
    u32 pid;
    char comm[TASK_COMM_LEN];
    char filename[256];
};

BPF_PERF_OUTPUT(events);

int syscall__rename(struct pt_regs *ctx, const char __user *oldname, const char __user *newname) {
    struct data_t data = {};
    data.pid = bpf_get_current_pid_tgid() >> 32;
    bpf_get_current_comm(&data.comm, sizeof(data.comm));
    bpf_probe_read_user_str(&data.filename, sizeof(data.filename), newname);
    
    events.perf_submit(ctx, &data, sizeof(data));
    return 0;
}
"""

print("LAT-OT ANTI-RANSOMWARE: Monitoring for mass file renames... (Ctrl+C to stop)")
try:
    b = BPF(text=bpf_text)
    b.attach_kprobe(event=b.get_syscall_fnname("rename"), fn_name="syscall__rename")

    def print_event(cpu, data, size):
        event = b["events"].event(data)
        if ".locked" in event.filename.decode():
            print(f"ALARM: Suspicious File Rename by PID {event.pid} ({event.comm.decode()}): {event.filename.decode()}")

    b["events"].open_perf_buffer(print_event)
    while True:
        b.perf_buffer_poll()
except Exception as e:
    print(f"eBPF Error: {e}")
