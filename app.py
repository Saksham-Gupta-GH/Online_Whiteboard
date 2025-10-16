from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "whiteboard_data.json"


def init_storage():
    """Create an empty data file if it doesn't exist."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)


@app.before_request
def ensure_data_file_exists():
    """Ensure the whiteboard data file exists before handling requests."""
    if not hasattr(app, "has_initialized"):
        init_storage()
        app.has_initialized = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/save", methods=["POST"])
def save_whiteboard():
    """Save drawn whiteboard data to file."""
    data = request.get_json()
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)
    return jsonify({"status": "success"})


@app.route("/load", methods=["GET"])
def load_whiteboard():
    """Load existing whiteboard data."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
