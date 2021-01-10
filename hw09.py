from flask import Flask,request
import datetime,time
app = Flask(__name__)


def get_week_day(date):
    week_day = {
    0: '星期一',
    1: '星期二',
    2: '星期三',
    3: '星期四',
    4: '星期五',
    5: '星期六',
    6: '星期日',
    }
    day = date.weekday() #weekday()可以獲得是星期幾
    return week_day[day]

def day():
    date=""
    for i in range(1,31):
        date=date+"<option>"+str(i)+"</option>"
    date=date+"</select>"
    return date



def Year():
    year=""
    for i in range(1980,2021):
        year=year+"<option>"+str(i)+"</option>"
    year=year+"</select>"
    return year    
    
def html():
    doc ='''
<FORM METHOD="POST">
Year:<select name ="year">
'''
    doc = doc + Year()
    doc=doc+"""
Month<select name="month" >
    <option>Jan</option>
    <option>Feb</option>
    <option>Mar</option>
    <option>Apr</option>
    <option>May</option>
    <option>Jun</option>
    <option>Jul</option>
    <option>Aug</option>
    <option>Sep</option>
    <option>Oct</option>
    <option>Nov</option>
    <option>Dec</option>
    </select>
Day:<select name="day">"""
    doc = doc +day()+"<INPUT TYPE=SUBMIT></form>"
    return doc


@app.route('/',methods=['GET','POST'])
def index():
    doc = html()
    if request.method == 'POST':
        year=int(request.form['year'])
        month=str(request.form['month'])
        day=int(request.form['day'])
        if(month=="Jan"):
            m=1
        if(month=="Feb"):
            m=2
        if(month=="Mar"):
            m=3
        if(month=="Apr"):
            m=4
        if(month=="May"):
            m=5
        if(month=="Jun"):
            m=7
        if(month=="Aug"):
            m=8
        if(month=="Sep"):
            m=9
        if(month=="Oct"):
            m=10
        if(month=="Nov"):
            m=11
        if(month=="Dec"):
            m=12

        today = datetime.datetime(int(year),m,int( day))
        todayis = get_week_day(today) 
        return doc+'Your birthday is '  + str(year) +'-'+ str(m)+'-' + str(day) + '. It is  ' + todayis
    
    return doc
