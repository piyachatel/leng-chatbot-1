#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request, abort
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
line_bot_api = LineBotApi('WjghX90v2F34cxZzGr1yZxcHX5l6UA+DaW6svTh1ifUTZqXIweGMSS0kVTZwLB+II6Ej3kxMpbehs6V6Uxx4YKNN9v1yqklxgpDpp6fuT+WTuZyylt69cVMVr93lyGOUCZlu8eZxZm2MfBCqW+hp1wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('1ae570f4539f531d46df94c38903c06f')
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
abort(400)
return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
line_bot_api.reply_message(
event.reply_token,
TextSendMessage(text=event.message.text))
if __name__ == "__main__":
   app.run()