from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "LINE Auto Estimator Bot is running."

@app.route("/webhook", methods=["POST"])
def webhook():
    body = request.get_data(as_text=True)
    print("Received Webhook:", body)
    return "OK", 200

if __name__ == "__main__":
    app.run()
