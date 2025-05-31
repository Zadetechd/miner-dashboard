from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

DATA_FILE = "data.json"

@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route("/api/update", methods=["POST"])
def update_data():
    try:
        data = request.json
        with open(DATA_FILE, "w") as f:
            json.dump(data, f)
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route("/api/stats", methods=["GET"])
def get_stats():
    if not os.path.exists(DATA_FILE):
        return jsonify({"hashrate": 0, "uptime": 0, "accepted": 0, "rejected": 0})
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
