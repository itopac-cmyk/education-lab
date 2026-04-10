# Dynamic Malware Analysis: Mastering GDB

To understand zero-day exploits (like the buffer overflow in `vulnerable_apps/`), we need **Dynamic Analysis** using the **GNU Debugger (GDB)**.

## 1. Preparation
Compile the vulnerable app with symbols and no protections:
```bash
cd vulnerable_apps
make
```

## 2. Running GDB
Start the debugger:
```bash
gdb ./vuln_buffer_overflow
```

### Essential Commands:
- `break process_input`: Set a breakpoint at the vulnerable function.
- `run $(python3 -c 'print("A"*20)')`: Run the app with a 20-character input (causing a 4-byte overflow).
- `info registers`: View the CPU registers (watch the `$eip` / `$rip`).
- `x/24wx $rsp`: Examine the stack memory.

## 3. Observing the Crash
When you provide a very long string (e.g., "A" * 40), the program will crash:
- `Program received signal SIGSEGV, Segmentation fault.`
- Look at the instruction pointer: If it shows `0x41414141` (AAAA), you have successfully overwritten the return address!

## 4. Exploitation Path (The Education Goal)
1.  **Find the Offset:** How many characters do we need to reach the return address?
2.  **Identify the Target Address:** Where should we redirect execution? (e.g., to our shellcode).
3.  **Construct the Payload:** [NOPSLED] + [SHELLCODE] + [TARGET ADDRESS].
