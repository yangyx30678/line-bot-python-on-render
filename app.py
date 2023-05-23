#linebotTest1
from flask import Flask
app = Flask(__name__)

#import flask
from flask import Flask, request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage


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
    my_text = event.message.text
    pic_url = ""
    # r = random.Random(30678)
    if my_text == "我想吃大餐":
        pic_index = 0
        with open('feast.txt') as f:
            lines = f.readlines()
            output = random.choice(lines)
            for index, x in enumerate(lines):
                if x == output:
                    pic_index = index
        with open('feast_pic.txt') as f:
            url_lines = f.readlines()
            pic_url = url_lines[pic_index]
        try:
            message = [
                TextSendMessage(
                    text=output
                    ),
                ImageSendMessage(
                original_content_url = pic_url,
                preview_image_url = pic_url
                    )
            ]
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token,
                TextSendMessage(text= '笑死 壞囉'))
    elif my_text == "我想吃小吃":
        pic_index = 0
        with open('streetfood.txt') as f:
            lines = f.readlines()
            output = random.choice(lines)
            for index, x in enumerate(lines):
                if x == output:
                    pic_index = index
        with open('streetfood_pic.txt') as f:
            url_lines = f.readlines()
            pic_url = url_lines[pic_index]
        try:
            message = [
                TextSendMessage(
                    text=output
                    ),
                ImageSendMessage(
                original_content_url = pic_url,
                preview_image_url = pic_url
                    )
            ]
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token,
                TextSendMessage(text= '笑死 壞囉'))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="呵呵"))


if __name__ == '__main__':
    app.run(port=8000)
    # port 8000 for render
    