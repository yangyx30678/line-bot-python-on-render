#linebotTest1
from flask import Flask
app = Flask(__name__)

#import flask
#XXXXXXX
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


@handler.add(MessageEvent, message=TextMessage)
#加入一個handle_message function
def handle_message(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))


if __name__ == '__main__':
    app.run()