from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/servers")
def servers():
    return jsonify({
        "servers": 69
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)