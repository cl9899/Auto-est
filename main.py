from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os
import json

app = Flask(__name__)

# 這兩個改成你自己的 LINE Channel Token / Secret
LINE_CHANNEL_ACCESS_TOKEN = "你的 channel access token"
LINE_CHANNEL_SECRET = "你的 channel secret"

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

@app.route("/", methods=["GET"])
def home():
    return "LINE Auto Estimator Backend OK"

@app.route("/webhook", methods=["POST"])
def webhook():
    body = request.get_data(as_text=True)
    print("Received Webhook:", body)
    signature = request.headers['X-Line-Signature']

    try:
        handler.handle(body, signature)
    except Exception as e:
        print("Error:", e)

    return "OK", 200

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    reply_text = f"你剛剛說的是：{user_message}"

    # 回覆使用者
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)
    )
import os
print("LINE_CHANNEL_SECRET =", os.getenv("LINE_CHANNEL_SECRET"))
print("SECRET =", os.getenv("LINE_CHANNEL_SECRET"))
print("LINE_SECRET = ", LINE_CHANNEL_SECRET)
