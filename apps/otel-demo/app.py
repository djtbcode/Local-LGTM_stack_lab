from flask import Flask
import random
import time

app = Flask(__name__)


@app.get("/")
def index():
    return {"message": "hello from otel-demo"}


@app.get("/slow")
def slow():
    time.sleep(random.uniform(0.2, 1.0))
    return {"message": "that was unnecessarily slow"}


@app.get("/error")
def error():
    raise RuntimeError("deliberate homelab error")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
