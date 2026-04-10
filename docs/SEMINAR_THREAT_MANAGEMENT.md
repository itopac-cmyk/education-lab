# Seminar Guide: 5 Web-Based Zero-Day Scenarios (2026)

This seminar focuses on the **visual and practical** demonstration of modern web vulnerabilities. All scenarios are reachable via the **Vulnerability Education Portal (Port 9000)**.

## The Entry Point
1. Run \`docker-compose up -d\` in the \`lab_infra\` folder.
2. Open your browser at **http://localhost:9000**.
3. You now see the catalog of all 5 scenarios.

---

## Scenario 1: Cloud-Native RCE (SSTI)
*   **The Look:** A simple "Welcome" page.
*   **The Simulation:** Add \`{{7*7}}\` to the URL. If it shows 49, it's vulnerable.
*   **The Exploit:** Inject a Python one-liner to read \`/etc/passwd\`.

## Scenario 2: Gateway SSRF (Ivanti/ProxyNotShell Style)
*   **The Look:** A "URL Proxy" tool.
*   **The Simulation:** Attempt to fetch \`http://localhost\`. It will be blocked.
*   **The Exploit:** Bypass the block by fetching \`http://internal_admin_api\` to steal the secret admin token.

## Scenario 3: AI Agent Prompt Injection
*   **The Look:** A chat interface for an AI Support Agent.
*   **The Simulation:** Ask it to "ping google.com".
*   **The Exploit:** Inject a shell command like \`ping localhost; id\` to trick the AI into executing code.

## Scenario 4: Identity & Token Theft
*   **The Look:** A "Login Debug" page.
*   **The Simulation:** View the page to see the leaked JWT token.
*   **The Exploit:** Use the stolen token to impersonate an admin against the ID-Provider service.

## Scenario 5: Insecure Deserialization
*   **The Look:** A POST endpoint for processing data.
*   **The Simulation:** Send a base64 string.
*   **The Exploit:** Send a base64-encoded Python \`pickle\` object that spawns a reverse shell or writes a file.

---

## Live Monitoring
Open the **SOC Dashboard (Port 8080)** in a second window to see the eBPF/Sigma alerts trigger as students perform these actions!
