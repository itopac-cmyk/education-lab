# Zero-Day-Lab: Adversary Emulation & Detection Engineering

[![Educational Use](https://img.shields.io/badge/Purpose-Education-green)](SECURITY.md)

## 🎯 Project Overview
This lab provides a modular framework to study the lifecycle of modern exploits and "virus-like" behaviors in a controlled environment. 

### Learning Objectives:
1.  **Vulnerability Research:** Understand memory corruption (Buffer Overflows) using GDB.
2.  **Exploit Chains:** How multiple vulnerabilities are chained to achieve Code Execution.
3.  **Adversary Emulation:** Simulating malware persistence and obfuscation (Payload Droppers, Persistence).
4.  **Detection Engineering:** Writing YARA and Sigma rules to stop the attack.

---

## 🏗️ Lab Components
- **/vulnerable_apps:** Intentionally flawed software to practice exploitation.
- **/exploit_sim:** Simulation of delivery (**payload_dropper.py**), exploitation, and persistence (**persistence_demo.sh**).
- **/detection:** YARA signatures for memory-based exploit detection.
- **/analysis:** Guides for **Dynamic Analysis (GDB)** and Reverse Engineering.

## 🎓 Academic Context
Designed for students and researchers to master the technical depth of **Offensive Security** within an ethical framework (M.Sc. Cyber Security).
