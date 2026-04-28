from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# 🔥 CORS แบบชัวร์สุด (Render + frontend ต่างโดเมน)
CORS(app, resources={r"/*": {"origins": "*"}})

# 📦 เก็บข้อมูลชั่วคราว (RAM)
stats = {
    "servers": 0,
    "users": 0
}

# 🟢 test route
@app.route("/")
def home():
    return jsonify({
        "message": "Candy API Online"
    })

# 📊 get stats
@app.route("/servers", methods=["GET"])
def servers():
    return jsonify(stats), 200

# 🔄 update stats
@app.route("/update", methods=["POST"])
def update():
    try:
        data = request.get_json(force=True)  # กัน JSON พัง

        stats["servers"] = int(data.get("servers", 0))
        stats["users"] = int(data.get("users", 0))

        return jsonify({
            "ok": True,
            "stats": stats
        }), 200

    except Exception as e:
        return jsonify({
            "ok": False,
            "error": str(e)
        }), 400


# 🚀 run (Render จะใช้ gunicorn อยู่แล้ว แต่เผื่อ local)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)