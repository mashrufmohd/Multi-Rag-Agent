from flask import Flask, request, jsonify
from flask_cors import CORS
from agents.agent_base import AgentManager
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

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

if __name__ == '__main__':
    app.run(debug=True)
