# Compile with security protections DISABLED for educational demo
# -fno-stack-protector: Disable Stack Canaries
# -z execstack: Allow code execution on the stack (NX disabled)
# -no-pie: Disable Address Space Layout Randomization (ASLR) impact for simpler demo

CC=gcc
CFLAGS=-fno-stack-protector -z execstack -no-pie -g

all: vuln_buffer_overflow

vuln_buffer_overflow: vuln_buffer_overflow.c
	$(CC) $(CFLAGS) vuln_buffer_overflow.c -o vuln_buffer_overflow

clean:
	rm -f vuln_buffer_overflow
