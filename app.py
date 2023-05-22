#linebotTest1
from flask import Flask
app = Flask(__name__)

#import flask
from flask import Flask, request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage


line_bot_api = LineBotApi('TjUdD+lC12qAYmVLoB0yJnu7TWSP6mkbHqRPpsVRid7coqsQ7ikywxfyXn+3ZlBuGMsnf8qCW8aCykv+ekI1xZ9BbaUzaFkQp3GYNzVKwU63Q1zqnqQWWGUjurhVvn3pEEA9pfMRJhAQluhpvusQoQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f2b089725e9ef1d7dfe05bd04a3c8f47')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    #獲得使用者輸入的訊息
    body = request.get_data(as_text=True)
    try:
        #送出訓席
        handler.handle(body, signature)
    except InvalidSignatureError:
        #送出Bad request (400)
        abort(400)
    
    #回覆OK
    return 'OK'

import random

@handler.add(MessageEvent, message=TextMessage)
#加入一個handle_message function
def handle_message(event):
    # line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text+"((歪頭((燦笑"))
    my_text = event.message.text
    if my_text == "我想吃大餐":
        with open('feast.txt') as f:
            lines = f.readlines()
            output = random.choice(lines)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=output))
    elif my_text == "我想吃小吃":
        with open('streetfood.txt') as f:
            lines = f.readlines()
            output = random.choice(lines)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=output))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text+"((歪頭((燦笑"))


if __name__ == '__main__':
    app.run(port=8000)