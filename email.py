from flask import Flask, render_template
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SENDER'] = '1106105340@nkust.ipv6.club.tw'
mail = Mail(app)

def send_email(to,subject,template,**kwargs):
    msg = Message(subject,sender=app.config['MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt',**kwargs)
    msg.html = render_template(template + '.html',**kwargs)
    mail.send(msg)


@app.route('/')
def index():
    return render_template('mail.html')



