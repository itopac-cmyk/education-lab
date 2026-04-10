from flask import Flask, render_template

app = Flask(__name__)

# Portfolio of the 5 Web Scenarios for the Seminar
SCENARIOS = [
    {
        "id": 1,
        "name": "Cloud-Native RCE (SSTI)",
        "description": "Exploit Template Injection in Jinja2 to gain shell access.",
        "url": "http://localhost:5000/vuln_ssti?name=Student",
        "tech": "Python/Flask/Jinja2"
    },
    {
        "id": 2,
        "name": "Gateway SSRF",
        "description": "Bypass filters to reach internal Admin APIs (Ivanti/Citrix Style).",
        "url": "http://localhost:5001/fetch?url=http://example.com",
        "tech": "Python/Urllib"
    },
    {
        "id": 3,
        "name": "AI Agent Prompt Injection",
        "description": "Trick an LLM Agent into executing unauthorized system commands.",
        "url": "http://localhost:5002/",
        "tech": "LLM/Subprocess/Regex"
    },
    {
        "id": 4,
        "name": "OAuth & JWT Token Theft",
        "description": "Leaking sensitive cloud identity tokens via directory traversal.",
        "url": "http://localhost:8000/debug?file=config.txt", # Port will be updated in docker-compose
        "tech": "JWT/OAuth/Auth0"
    },
    {
        "id": 5,
        "name": "Insecure Deserialization",
        "description": "Executing code by sending malicious base64-encoded Python objects.",
        "url": "http://localhost:5000/vuln_deserialize",
        "tech": "Python/Pickle/Base64"
    }
]

@app.route('/')
def index():
    return render_template('index.html', scenarios=SCENARIOS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
