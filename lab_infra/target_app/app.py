from flask import Flask, request, render_template_string, render_template
import base64
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Zero-Day-Lab: Vulnerable Target Environment</h1><p>Check /vuln_ssti?name=Student</p>"

# Vulnerability 1: Server-Side Template Injection (SSTI)
@app.route('/vuln_ssti')
def ssti():
    name = request.args.get('name', 'Guest')
    # NEVER pass user input directly into render_template_string!
    template = f"<h2>Welcome, {name}!</h2><p>We are running a custom Flask backend.</p>"
    try:
        return render_template_string(template)
    except Exception as e:
        return str(e)

# Vulnerability 2: Insecure Deserialization
@app.route('/vuln_deserialize', methods=['POST'])
def deserialize():
    try:
        data = request.form.get('data')
        decoded = base64.b64decode(data)
        # Insecure use of pickle allows arbitrary code execution
        obj = pickle.loads(decoded)
        return f"Deserialized: {obj}"
    except Exception as e:
        return "Error decoding data."

if __name__ == '__main__':
    # Run openly in the container
    app.run(host='0.0.0.0', port=5000)
