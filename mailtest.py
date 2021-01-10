from flask_mail import Mail, Message
from flask import Flask, render_template,request
app = Flask(__name__)
app.config['MAIL_SENDER'] = 'nkust@ns16.ipv6.club.tw'
mail = Mail(app)




def send_email(to,subject,template,**kwargs):
    msg = Message(subject,sender=app.config['MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt',**kwargs)
    msg.html = render_template(template + '.html',**kwargs)
    mail.send(msg)




@app.route('/')
def index():
    name = 'david'
    send_email('1106105340@nkust.edu.tw','Midterm Exam' , 'midterm' , name=name,grade=90)
    
    return 'Mail sent to {}. '.format(name)
