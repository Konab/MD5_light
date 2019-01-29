# from threading import Thread
# from flask_mail import Message
# from app import mail
# from md5_light import app
# # from flask import current_app


# # def send_async_email(app, msg):
# #     with app.app_context():
# #         mail.send(msg)


# def send_email(subject, sender, recipients, text_body):
#     # msg = Message(subject, sender=sender, recipients=[recipients])
#     # msg.body = text_body
#     # with app.app_context():
#     # 	mail.send(msg)
#     # # Thread(target=send_async_email, args=(app, msg)).start()
# 	msg = Message("Hello",
#                   sender="from@example.com",
#                   recipients=["konab-job@yandex.ru"])
# 	msg.body = "testing"
# 	msg.html = "<b>testing</b>"
# 	mail.send(msg)
from threading import Thread
from flask import current_app
from md5_light import app
from flask_mail import Message
from app import mail


def send_email(subject, sender, recipients, text_body, app):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    with app.app_context():
      mail.send(msg)