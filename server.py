from flask import Flask, request, jsonify
from flask_cors import CORS
from agents.agent_base import AgentManager
import os
import time
import logging

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

agent_manager = AgentManager(max_retries=2, verbose=True)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        main_agent = agent_manager.get_agent("summarize")
        validator_agent = agent_manager.get_agent("summarize_validator")
        
        summary = main_agent.execute(f"Summarize the following text:\n{text}")
        validation = validator_agent.execute(text, summary)

        return jsonify({"summary": summary, "validation": validation})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.before_request
def start_timer():
    """Start timing before handling the request."""
    request.start_time = time.time()

@app.after_request
def log_request_time(response):
    """Log the response time after the request is processed."""
    elapsed_time = time.time() - request.start_time
    logging.info(f"Request {request.path} processed in {elapsed_time:.4f} seconds")
    return response

@app.route('/process', methods=['POST'])
def process():
    """Example API route to test response time logging."""
    time.sleep(1)  # Simulate processing delay
    return jsonify({"message": "Processed successfully"})

if __name__ == '__main__':
    app.run(debug=True)
