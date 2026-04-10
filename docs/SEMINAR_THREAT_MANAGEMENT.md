# Seminar: Advanced Threat Management & Ethical Hacking (2026)

This guide provides a roadmap for demonstrating complex, modern attack chains and their detection.

## Module 1: The Modern Supply Chain Attack (XZ Utils Style)
**Concept:** Attackers no longer target the front door; they target the tools you trust.
*   **The Scenario:** A popular Go crypto library (\`vulnerable_apps/supply_chain_lib/backdoor.go\`) is compromised. It exfiltrates secrets when used.
*   **The Demo:** Show how the backdoor is hidden in a benign function. Explain why traditional SCA (Software Composition Analysis) often misses logic-based backdoors.
*   **Threat Management:** Discuss the move towards **Software Bill of Materials (SBOM)** and binary attestation in 2026.

## Module 2: Identity is the Perimeter (OAuth & Token Theft)
**Concept:** In the cloud, IP addresses are irrelevant. Identity tokens are everything.
*   **The Attack:** An attacker uses a small directory traversal flaw in the \`web_app_cloud\` to read \`/app/token.txt\`. 
*   **The Impact:** With this token, the attacker can authenticate to the \`id_provider\` as an admin.
*   **Ethical Hacking:** Demonstrate the token theft using \`curl\`.
*   **Threat Management:** Discuss **Zero Trust Architecture (ZTA)** and why tokens should be short-lived and hardware-bound.

## Module 3: Live Threat Visualization (The SOC Dashboard)
**Concept:** Detection is only useful if it's actionable.
*   **The Setup:** Open the SOC Dashboard at \`http://localhost:8080\`.
*   **The Demo:** Run an exploit (e.g., Scenario 1: SSTI). Show the eBPF alert appearing in real-time.
*   **Threat Management:** Discuss **Alert Fatigue** and how automated triage (using your LAT-OT project!) can help analysts focus on critical threats.

## Module 4: Future Zero-Days (Memory Safety & Side-Channels)
**Concept:** Why do we still have Zero-Days in 2026?
1.  **Legacy Codebases:** Millions of lines of C/C++ in core infrastructure (Kernel, OpenSSL).
2.  **Memory Safety:** Discuss the transition to **Rust** and why it eliminates 70% of classic vulnerabilities.
3.  **Hardware-Assisted Side-Channels:** Briefing on new Spectre/Meltdown variants targeting modern AI chips.
