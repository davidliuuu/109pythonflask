from flask import Flask,request
app = Flask(__name__)

@app.route('/')
def index():
   doc ='''<FORM METHOD=POST ACTION =add>
<INPUT TYPE=TEXT NAME=a>
<INPUT TYPE=TEXT NAME=b>
<INPUT TYPE=SUBMIT>'''
   return doc

@app.route('/add',methods=['GET','POST'])
def add():
   a=int(request.args['a'])
   b=int(request.args['b'])
   doc ="{}+{}={}".format(a,b,a+b)
   return doc
