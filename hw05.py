
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/nine/<int:n>')
def nine(n):
    return render_template('hw05.html',range=range(1,n+1))
