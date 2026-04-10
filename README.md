# Zero-Day-Lab: Modern Adversary Emulation & Detection Engineering (2026 Edition)

[![Educational Use](https://img.shields.io/badge/Purpose-Education-green)](SECURITY.md)
[![Tech Stack](https://img.shields.io/badge/Tech-Docker%20%7C%20Go%20%7C%20eBPF%20%7C%20Python-blue)]()

## 🎯 Project Overview
This lab is a comprehensive framework for studying the lifecycle of modern exploits. It moves beyond classic buffer overflows into the realm of **Cloud-Native Exploitation (SSTI, Deserialization)**, **EDR Evasion (Go-Malware)**, and **Kernel-Level Detection (eBPF)**. 

Instead of focusing purely on "how to attack," we focus on **"how to detect and mitigate."**

### Core Learning Objectives:
1.  **Vulnerability Research:** Understand modern web flaws (SSTI, Insecure Deserialization).
2.  **Adversary Emulation:** Simulating modern malware behaviors (Sleep Obfuscation, C2 Fetching) using Go.
3.  **Detection Engineering:** Writing SIEM detections (Sigma) and Kernel-level monitoring (eBPF/BCC).

---

## 🏗️ Lab Infrastructure
The lab is built on Docker Compose to provide an instant, safe, and realistic enterprise environment.

### Components:
- **`/lab_infra`:** Contains `docker-compose.yml` to launch the vulnerable `target_app` (Flask) and an `attacker_node`.
- **`/vulnerable_apps`:** Classic memory corruption examples (C/Buffer Overflows) for foundational learning.
- **`/exploit_sim`:** 
  - `modern_dropper_go/`: A Go-based malware dropper simulating EDR evasion.
  - `payload_dropper.py` / `persistence_demo.sh`: Scripted adversary techniques.
- **`/detection`:** 
  - `ebpf_monitor/`: Real-time kernel syscall hooking (`execve`) using Python and BCC.
  - `sigma_rules/`: Enterprise SIEM detection logic.
  - `yara_rules.yar`: Memory and file scanning signatures.

---

## 🚀 Quick Start (Demo Scenario)
Want to see an exploit and its detection in action? 
Follow the detailed guide in: **[Scenario 1: Cloud-Native RCE via SSTI](docs/SCENARIO_1_SSTI_TO_RCE.md)**

## 🎓 Academic Context
Designed for students and researchers to master the technical depth of **Offensive Security** within an ethical framework (M.Sc. Cyber Security).
