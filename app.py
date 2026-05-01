from flask import Flask
import os

app = Flask(__name__)

VERSION = os.environ.get("APP_VERSION", "v1")

@app.route("/")
def hello():
    return f"Hello from ECS Lab - {VERSION}\n"

@app.route("/health")
def health():
    return "OK\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
