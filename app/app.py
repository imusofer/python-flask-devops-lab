from flask import Flask, jsonify
import os
from datetime import datetime, UTC
from zoneinfo import ZoneInfo

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Python DevOps Lab App</h1>
    <p>This is the home page of my first Flask app.</p>
    <ul>
        <li><a href="/health">/health</a></li>
        <li><a href="/config">/config</a></li>
        <li><a href="/time">/time</a></li>
    </ul>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/config")
def config():
    environment = os.getenv("APP_ENV", "dev")
    version = os.getenv("APP_VERSION", "1.0.0")

    return jsonify({
        "environment": environment,
        "version": version,
        "hostname": os.uname().nodename
    })


@app.route("/time")
def time():
    return jsonify({
        "current_utc_time": datetime.now(UTC).isoformat(),
        "current_sofia_time": datetime.now(ZoneInfo("Europe/Sofia")).isoformat()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)