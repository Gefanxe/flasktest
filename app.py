from flask import Flask, request, abort
from datetime import datetime

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('zSKBwPSS6xHM8P5jNiY8URDPteb+cUkxXej+DgrRTRa/bQaZIK+JCnV7dTjWz8Tfg52aGQhYy0QrjxYqDQG91QJvFW0M84fT8qrlRuq3C4f8sU/W8bBytwpbJCmnY/Xi/FdELJ1ZgH3B1cP0UgOGYQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7cd300df3806d160948ab5609a06ef78')

@app.route('/')
def hello_world():
    now = datetime.now()
    return f'Hello, World! {now.strftime("%Y-%m-%d %H:%M:%S")}'

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()