from flask import Flask,render_template,redirect,url_for,request
import datetime
app = Flask(__name__)

def nowtime():
    x = datetime.datetime.now() 
    y= "{"+str(x.year)+"/"+str(x.month)+"/"+str(x.day)+" "+str(x.hour)+":"+str(x.minute)+":"+str(x.second)+"}"
    return y



@app.route('/')
def index():
    return render_template('hw06.html')

@app.route('/main/<int:n>')
def main(n):
    if n==1:
        ip = request.remote_addr
        time=nowtime()
        iptime=ip+" "+time+" "+"https://www.youtube.com/"
        print(iptime)
        return redirect('https://www.youtube.com/')
    elif n==2:
        ip = request.remote_addr
        time=nowtime()
        iptime=ip+" "+time+" "+"https://www.nkust.edu.tw/"
        print(iptime)
        return redirect('https://www.nkust.edu.tw/')
    elif n==3:
        ip = request.remote_addr
        time=nowtime()
        iptime=ip+" "+time+" "+"https://cnn.com"
        print(iptime)
        return redirect('https://cnn.com')
