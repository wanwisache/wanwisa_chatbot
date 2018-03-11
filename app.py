from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)

app = Flask(__name__)

line_bot_api = LineBotApi('l1iSRZNSDMEDq4hY91lS2/z9B38u36+TBfuiwT0vaYzv01//3aZoIg/ynFPbz6ivwT2cXxF9VTP7DBLsLCdtAxkuoaML/BLzoUnVW3eDBXoKkZKlfD77NQXm9S1NlVpB9H3RP9E+XafeY/4uiLEeIQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('bf02eb5b1c90978bff10a1fd96c8d31f')

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/webhook", methods=['POST'])
def webhook():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
    

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
