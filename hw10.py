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
    Month=SelectField('mouth',choices=[('Jan'),('Feb'),('Mar'),('Apr'),('May'),('Jun'),('Jul'),('Aug'),('Sep'),('Oct'),('Nov'),('Dec')])
    Day=SelectField('Day',choices=date)
    Submit=SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    form=UserForm()
    if form.validate_on_submit():
        year =request.form.get("Year")
        month =request.form.get("Month")
        day =request.form.get("Day")
    return render_template('index.html',form=form)
	
