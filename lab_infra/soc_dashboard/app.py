from flask import Flask, render_template, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

# Simulated log storage for the demo
LOG_FILE = "/app/logs/alerts.json"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/alerts')
def get_alerts():
    if not os.path.exists(LOG_FILE):
        return jsonify([])
    with open(LOG_FILE, 'r') as f:
        try:
            alerts = json.load(f)
            return jsonify(alerts[-20:]) # Return last 20 alerts
        except:
            return jsonify([])

if __name__ == '__main__':
    # Initialize log file
    os.makedirs("/app/logs", exist_ok=True)
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w') as f:
            json.dump([], f)
    app.run(host='0.0.0.0', port=8080)
