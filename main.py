
from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received webhook:", data)
    return "OK"

@app.route("/", methods=["GET"])
def home():
    return "AutoBot Estimator Webhook is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
