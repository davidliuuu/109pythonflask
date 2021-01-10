from flask import Flask,request
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY']='hard to guess string'
year1 =[i for i in range(1980,2021)]
date =[i for i in range(1,32)]
class UserForm(FlaskForm):
    Year=SelectField('Year',choices=year1)
    Month=SelectField('mouth',choices=[('Jan'),('Feb'),('Mar'),('Apr'),('May'),(
'Jun'),('Jul'),('Aug'),('Sep'),('Oct'),('Nov'),('Dec')])
    Day=SelectField('Day',choices=date)
    submit=SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    form=UserForm()
    return render_template('hw11.html',form=form)
