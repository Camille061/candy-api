from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

stats = {"servers": 100, "users": 3413}

@app.after_request
def add_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.route("/servers")
def servers():
    return jsonify(stats)

@app.route("/update", methods=["POST"])
def update():
    data = request.get_json(force=True)
    stats["servers"] = data.get("servers", 0)
    stats["users"] = data.get("users", 0)
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)