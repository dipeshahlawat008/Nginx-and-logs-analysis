from flask import Flask, jsonify
from core.health_monitor import sample_system
from core.analyzer import analyze_log_file
import threading

app = Flask(__name__)

@app.route('/health')
def health():
    data = sample_system()
    return jsonify(data)

@app.route('/analyze')
def analyze():
    # For simplicity analyze sample.log
    analyze_log_file('sample.log')
    return jsonify({'status':'analysis_started'})

def run_api():
    app.run(host='0.0.0.0', port=8000, debug=False)

if __name__ == '__main__':
    run_api()
