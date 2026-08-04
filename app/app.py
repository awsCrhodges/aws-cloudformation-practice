from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def health():
    return jsonify(
        message="Container is running in Amazon ECS"
        status="healthy"
    )

if __name___ == "__main__":
    app.run(host="0.0.0.0", port=8080)