from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Flask App"
    })

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return jsonify({
        "num1": a,
        "num2": b,
        "result": a + b
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)