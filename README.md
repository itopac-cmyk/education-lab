# Zero-Day-Lab: Professional Cyber Security Education (Seminar Edition)

[![Educational Use](https://img.shields.io/badge/Purpose-Education-green)](SECURITY.md)
[![Status](https://img.shields.io/badge/Status-Seminar%20Ready-blue)](docs/SEMINAR_THREAT_MANAGEMENT.md)

## 🎯 The Seminar Entry Point
For a high-impact demo, use our **Vulnerability Education Portal**:
1. \`cd lab_infra && docker-compose up -d\`
2. Open **http://localhost:9000** in your browser.

---

## 🏗️ 5 Web-Based Zero-Day Scenarios (Live Demos)
Our lab provides a containerized microservice environment to simulate the mechanics of:
1.  **[Cloud-Native RCE (SSTI):](docs/SCENARIO_1_SSTI_TO_RCE.md)** Injection into template engines.
2.  **[Gateway SSRF:](docs/scenarios/SCENARIO_2_SSRF_TO_RCE.md)** Bypassing edge security to pivot internally.
3.  **[Agentic AI Prompt Injection:](docs/scenarios/SCENARIO_3_LLM_AGENT_EXPLOIT.md)** Trick AI agents into system-level execution.
4.  **[OAuth Identity Theft:](lab_infra/auth_service/)** Stealing cloud tokens via misconfigurations.
5.  **[Insecure Deserialization:](lab_infra/target_app/app.py)** Code execution via unsafe object loading.

---

## 🛡️ Live Threat Management Dashboard
Visualize alerts in real-time at **http://localhost:8080** as you run the exploits. Our **eBPF Kernel Monitor** and **Sigma rules** track every hacker action.

---

## 🎓 Academic Context
Developed by **Isato Pac** for the **M.Sc. Cyber Security** at **Hochschule Aalen** (April 2026).
