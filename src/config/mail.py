from flask_mail import Mail, Message
from flask import render_template

mail = Mail()

class Mail():
    def resetPassword(email, token):
        message = Message()
        message.subject = "Reset Password Link"
        message.recipients = [email]
        message.sender = "noreply@sibi.com"
        message.html = render_template("emails/reset_password.html", token=token)
        
        return message
        
    def sendMessage(message):
        mail.send(message)
    