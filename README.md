# Zero-Day-Lab: Professional Cyber Security Education (Seminar Edition)

[![Educational Use](https://img.shields.io/badge/Purpose-Education-green)](SECURITY.md)
[![Status](https://img.shields.io/badge/Status-Seminar%20Ready-blue)](docs/SEMINAR_THREAT_MANAGEMENT.md)

## 🎯 The Seminar-Ready Lab
This lab is a comprehensive framework for **Threat Management** and **Ethical Hacking** seminars. It provides a containerized microservice environment to demonstrate the mechanics of the most devastating attacks from 2020-2026.

### Advanced Seminar Modules:
1.  **[Supply Chain Attacks:](vulnerable_apps/supply_chain_lib/)** XZ Utils / Log4j style backdoor simulation.
2.  **[Identity & OAuth Exploitation:](lab_infra/auth_service/)** Bypassing perimeters via Token Theft.
3.  **[Ransomware & EDR:](docs/scenarios/SCENARIO_4_RANSOMWARE.md)** Automated encryption and eBPF-based detection.
4.  **[Hardware Side-Channels:](docs/scenarios/SCENARIO_5_HARDWARE_EXPLOITS.md)** Leakage via CPU Cache timing (Spectre/Meltdown).
5.  **[Agentic AI Prompt Injection:](docs/scenarios/SCENARIO_3_LLM_AGENT_EXPLOIT.md)** Exploiting LLMs with system access.
6.  **[Cloud-Native RCE & SSRF:](docs/scenarios/SCENARIO_2_SSRF_TO_RCE.md)** Gateway exploitation and pivoting.

---

## 🛡️ Live Threat Management Dashboard
The lab includes a **real-time SOC Dashboard** (Port 8080) that visualizes alerts from our **eBPF Kernel Monitor** and **Sigma detection rules**. 

---

## 🏗️ Lab Infrastructure
- **\`/lab_infra\`:** Docker-compose setup for the entire range.
- **\`/vulnerable_apps\`:** Source code for flawed, backdoored, and hardware-leaking apps.
- **\`/detection\`:** Kernel-level (eBPF) and SIEM-level (Sigma/YARA) detection logic.
- **\`/analysis\`:** Guides for Dynamic Analysis (GDB) and Forensics.

## 🚀 Quick Start for Instructors
1. \`cd lab_infra && docker-compose up -d\`
2. Follow the **[Seminar Guide](docs/SEMINAR_THREAT_MANAGEMENT.md)** and the **[Scenarios](docs/scenarios/)**!
