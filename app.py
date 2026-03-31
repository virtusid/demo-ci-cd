from flask import Flask, jsonify, render_template
import os
import socket

app = Flask(__name__)

APP_VERSION = "1.0.0"
POD_NAME = socket.gethostname()
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

@app.route("/")
def index():
    return render_template("index.html",
        version=APP_VERSION,
        pod_name=POD_NAME,
        environment=ENVIRONMENT
    )

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/info")
def info():
    return jsonify({
        "version": APP_VERSION,
        "pod": POD_NAME,
        "environment": ENVIRONMENT
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
