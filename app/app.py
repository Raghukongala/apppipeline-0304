from flask import Flask, jsonify
import os
import socket
import logging
from datetime import datetime

app = Flask(__name__)

# Logging setup (important for ECS logs)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Environment variables
APP_NAME = os.getenv("APP_NAME", "ECS Microservice")
VERSION = os.getenv("VERSION", "1.0")
ENV = os.getenv("ENV", "dev")

@app.route("/")
def home():
    logger.info("Home endpoint hit")

    return jsonify({
        "message": f"Hello Deepthi 👋 from {APP_NAME} 🚀",
        "status": "running",
        "version": VERSION,
        "environment": ENV,
        "hostname": socket.gethostname(),
        "timestamp": datetime.utcnow().isoformat()
    })


@app.route("/health")
def health():
    logger.info("Health check endpoint hit")

    return jsonify({
        "status": "OK",
        "service": APP_NAME,
        "time": datetime.utcnow().isoformat()
    }), 200


@app.route("/info")
def info():
    return jsonify({
        "app": APP_NAME,
        "version": VERSION,
        "environment": ENV,
        "host": socket.gethostname()
    })


@app.route("/error")
def error():
    # Test endpoint for failure scenarios (for monitoring)
    return jsonify({"error": "Simulated error"}), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    logger.info(f"Starting {APP_NAME} on port {port}")
    
    app.run(host="0.0.0.0", port=port, debug=False)
