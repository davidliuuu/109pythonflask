from flask import Flask,request
import sqlite3
app = Flask(__name__)

conn = sqlite3.connect("hw14.db")
cursor = conn.cursor()
stmt = "SELECT 學校名稱,SUM(總計) FROM student Group BY 學校名稱 ORDER BY SUM(總計)"
cursor.execute(stmt)
sum=[]
school=[]
ckk=[]
ck=0
for row in cursor.fetchall():
    ck=ck+1
    a,b=row
    school.append(a)
    sum.append(b)
    ckk.append(ck)
conn.close()



@app.route('/')
def html():
   doc ='''<FORM METHOD=POST ACTION =menu>
校名<INPUT TYPE=TEXT NAME=a><br>
<INPUT TYPE=SUBMIT>'''
   return doc



@app.route('/menu',methods=['GET','POST'])
def menu():
   count=0;
   doc='''<FORM METHOD=POST ACTION =sol>

 多個選項<br>       
'''
   


   if request.method == 'POST':
      a=str(request.form['a'])
      for i in range(1,len(school)):
          if a in school[i]:
             b=school[i]
             count=count+1 
             doc = doc+'<input  type="radio" name="school" value={}>{}<br>'.format(school[i],school[i])
      doc=doc+'<INPUT TYPE=SUBMIT>'
      if count!=1: 
         return doc;
      else:
         conn = sqlite3.connect("hw14.db")
         cursor = conn.cursor()
         stmt = "SELECT 學校名稱,SUM(總計) AS total FROM student Group BY 學校名稱 ORDER BY Total ASC"
         cursor.execute(stmt)
         c=0
         dd='<table BORDER=1>'
         itt='''<tr>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                </tr>'''
         itt2='''<tr><td bgcolor="red">{}</td>
                 <td bgcolor="red">{}</td>
                 <td bgcolor="red">{}</td>
                 </tr>'''
         level=[]
         sch=[]
         summ=[]
         for row in cursor.fetchall():
             c=c+1
             k,q=row
             level.append(c)
             sch.append(k)
             summ.append(q)
             if b==k:
                x=c
         conn.close() 
         for i in range(x-10,x+10):
             if i>0 and i<len(level):
                if i==x-1:
                   dd=dd+itt2.format(level[i],sch[i],summ[i])
                else:
                   dd=dd+itt.format(level[i],sch[i],summ[i])  
         return dd+'</table>';
@app.route('/sol',methods=['GET','POST'])
def sol():
   x=0
   b=str(request.form['school'])
   dd='<table BORDER=1>'
   itt='''<tr>
          <td>{}</td>
          <td>{}</td>
          <td>{}</td>
          </tr>'''
   itt2='''<tr><td bgcolor="red">{}</td>
           <td bgcolor="red">{}</td>
           <td bgcolor="red">{}</td>
           </tr>'''
   
   for i in range(1,len(school)):
       if b==school[i]:
          x = ckk[i]
   for i in range(x-10,x+10):
       if i>0 and i<len(ckk):
          if i==x-1:
             dd=dd+itt2.format(ckk[i],school[i],sum[i])
          else:
             dd=dd+itt.format(ckk[i],school[i],sum[i]) 
   return dd+'</table>';

