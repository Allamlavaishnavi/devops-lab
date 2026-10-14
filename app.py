
from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = "1.0"


@app.route("/")
def home():
    return f"""
    <h1>Batch 9 DevOps Project</h1>
    <p>Flask application deployed using Docker and Jenkins.</p>
    <p>Application Version: {APP_VERSION}</p>
    """


@app.route("/health")
def health():
    return jsonify(
        status="healthy",
        version=APP_VERSION
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
