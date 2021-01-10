from flask import Flask,request
app = Flask(__name__)

@app.route('/')
def index():
   doc ='''<FORM METHOD=POST ACTION =bmi>
身高<INPUT TYPE=TEXT NAME=a>公分(cm)<br>
體重<INPUT TYPE=TEXT NAME=b>公斤(kg)<br>
<INPUT TYPE=SUBMIT>'''
   return doc

@app.route('/bmi',methods=['GET','POST'])
def bmi():
   a=float(request.form['a'])
   a=a/100
   b=float(request.form['b'])
   bmi = float(b/(a**2))
   bmi = round(bmi,2)
   bmi = str(bmi)
   doc ="you bmi = {}".format(bmi)
   return doc
