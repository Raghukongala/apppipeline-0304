from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello Raghuramrajarhahahhaahjafrom ECS Microservice 🚀",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "OK"
    })

if __name__ == "__main__":
    # Runs the Flask app inside Docker container
    app.run(host="0.0.0.0", port=5000, debug=False)
