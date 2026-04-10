# Scenario 4: Ransomware Lifecycle & Real-Time EDR Detection

This scenario demonstrates the critical phase of a ransomware attack: automated encryption and how modern EDR (Endpoint Detection & Response) detects this behavior on the kernel level.

## The Goal
Execute a simulated ransomware binary and observe how an eBPF-based monitor detects mass file renaming (the ".locked" pattern).

## Step 1: Prepare the Target Data
Initialize a test directory with dummy files:
```bash
# Data is already initialized in data/test_vault/
ls data/test_vault/
```

## Step 2: Start the Defense (eBPF Monitor)
On the host machine (requires root):
```bash
sudo python3 detection/ebpf_monitor/file_monitor.py
```

## Step 3: Run the Attack (Ransomware Simulator)
In a second terminal:
```bash
cd exploit_sim/ransomware_go
go run main.go
```

## Step 4: The Result
1. **The Attacker:** The Go binary traverses the directory and renames every file to \`.locked\`.
2. **The Defender:** The eBPF monitor immediately detects each rename on the syscall level and triggers an alarm: **"ALARM: Suspicious File Rename..."**.
3. **The SOC:** The SOC Dashboard (Port 8080) would receive these alerts in a real setup.

## Step 5: Post-Exploitation
Check the "Ransom Note":
```bash
cat data/test_vault/README_FOR_DECRYPT.txt
```
