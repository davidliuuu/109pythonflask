from flask import Flask,request
import datetime
app = Flask(__name__)

def nowdate():
    x = datetime.datetime.now() 
    y= str(x.year)+"-"+str(x.month)+"-"+str(x.day)
    return y

def nowtime():
    x = datetime.datetime.now() 
    y= str(x.hour)+":"+str(x.minute)
    return y

def loadtxt():
    x=[]
    date=[]
    time=[]
    item=[]
    counter=[]
    html_table=''
    infile= open("hw08.txt",'r')
    for line in infile:
        x.append(line)
    infile.close()
    print(len(x))
    if len(x)!=0:
        for i in range(0,len(x)):
            u1,u2,u3,u4 = x[i].split(' ',3)
            date.append(u1)
            time.append(u2)
            item.append(u3)
            counter.append(u4)
        for j in range(0,len(x)):
            html_table += '''
<TR>
    <TD>{}</TD>
    <TD>{}</TD>
    <TD>{}</TD>
    <TD>{}</TD>
</TR>
'''.format(date[j],time[j],item[j],counter[j])
    return html_table


html_tableend="</table></div></div>"
nowdate = nowdate()
tim = nowtime()


@app.route('/',methods=['GET','POST'])
def index():
    html_table=loadtxt()

    doc ='''
<FORM METHOD="POST" >
<div style="width:900px">
<div style="position:absolute;top:30%;left:10%;">
日期<INPUT TYPE=TEXT NAME=a value={} ><br>
時間<INPUT TYPE=TEXT NAME=b value={}><br>
運動項目<select name="sport" >
    <option></option>
    <option>跑步</option>
    <option>打籃球</option>
    <option>仰臥起坐</option>
    </select><br>
次數 or 時間  <INPUT TYPE=TEXT NAME=c><br>
<INPUT TYPE=SUBMIT>
</div>
<div style = "float:right">
<TABLE BORDER=1 ALIGN=right>
<TR>
    <TD>日期</TD>
    <TD>時間</TD>
    <TD>運動項目</TD>
    <TD>次數 or 時間</TD>
</TR>
'''.format(nowdate,tim)
    
    olddoc = doc + html_table + html_tableend
    
    if request.method == 'POST':
        a=str(request.form['a'])
        b=str(request.form['b'])
        c=str(request.form['c'])
        sport=str(request.form['sport'])
        infile = open('hw08.txt', 'a')
        info=a+" "+b+" "+sport+" "+c+"\n"
        infile.write(info)
        infile.close()
        html_table=loadtxt()
        newdoc= doc + html_table + html_tableend
        return newdoc

    return olddoc







