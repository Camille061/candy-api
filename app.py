from flask import Flask, jsonify, request

app = Flask(__name__)

stats = {"servers": 0, "users": 0}

@app.route("/")
def home():
    return "Candy API Online"

@app.route("/servers")
def servers():
    return jsonify(stats)

@app.route("/update", methods=["POST"])
def update():
    data = request.json
    stats["servers"] = data.get("servers", 0)
    stats["users"] = data.get("users", 0)
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)