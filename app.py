from flask import Flask, render_template, request, jsonify
import sqlite3
import json
import os

app = Flask(__name__)

# Get absolute path to ensure DB works on Render
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "whiteboard.db")

# Initialize DB
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS boards (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    data TEXT
                )''')
    conn.commit()
    conn.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save():
    content = request.json
    board_name = content.get("name", "Untitled")
    data = json.dumps(content.get("data", {}))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO boards (name, data) VALUES (?, ?)", (board_name, data))
    conn.commit()
    conn.close()

    return jsonify({"status": "success", "message": "Board saved!"})

@app.route("/load", methods=["GET"])
def load():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, name FROM boards")
    boards = [{"id": row[0], "name": row[1]} for row in c.fetchall()]
    conn.close()
    return jsonify(boards)

@app.route("/load/<int:board_id>", methods=["GET"])
def load_board(board_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT data FROM boards WHERE id=?", (board_id,))
    row = c.fetchone()
    conn.close()
    if row:
        return jsonify(json.loads(row[0]))
    return jsonify({"error": "Board not found"}), 404

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=10000)
