from flask import Flask, render_template,request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SENDER'] = 'nkust@ns16.ipv6.club.tw'
mail = Mail(app)

def send_email(to,subject,template,**kwargs):
    msg = Message(subject,sender=app.config['MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt',**kwargs)
    msg.html = render_template(template + '.html',**kwargs)
    mail.send(msg)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
       email = str(request.form['a'])
       name = str(request.form['b'])
       grade = str(request.form['c'])
       send_email(email,'Midterm Exam' , 'midterm' , name=name,grade=grade)
       return 'Mail sent to {}. '.format(name)
    else:
       return render_template('mail.html')  
