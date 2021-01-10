from flask import Flask,request
import sqlite3
app = Flask(__name__)


conn = sqlite3.connect("passwd.db")
cursor = conn.cursor()
stmt = "SELECT * FROM user"
cursor.execute(stmt)
username=[]
password=[]
for row in cursor.fetchall():
    a,b=row
    username.append(a)
    password.append(b)
conn.close()




@app.route('/')
def html():
   doc ='''<FORM METHOD=POST ACTION =menu>
Username<INPUT TYPE=TEXT NAME=a><br>
Password<INPUT TYPE=TEXT NAME=b><br>
<INPUT TYPE=SUBMIT>'''
   return doc

@app.route('/menu',methods=['GET','POST'])
def menu():
   a=str(request.form['a'])
   b=str(request.form['b'])
   for i in range(0,len(username)):
     if a==username[i] and b==password[i]:
        doc='''1.<a href="http://nkust.ipv6.club.tw:10640/main/1">Intro</a><br>2.<a href="http://nkust.ipv6.club.tw:10640/main/2">Change Password</a><br>'''
        return doc
     else:
        doc ='使用者帳密錯誤'
        return doc

@app.route('/main/<int:n>',methods=['GET','POST'])
def main(n):
    if n==1:
       return 'Hello'
    elif n==2:
       doc ='''<FORM METHOD=POST>
Change Password<br>
Username <INPUT TYPE=TEXT NAME=a><br>
Old Password<INPUT TYPE=TEXT NAME=b><br>
New Password<INPUT TYPE=TEXT NAME=c><br>
Confirme Password<INPUT TYPE=TEXT NAME=d><br>
<INPUT TYPE=SUBMIT>'''
       if request.method == 'POST':
          username1=str(request.form['a'])
          oldpassword=str(request.form['b'])
          newpassword=str(request.form['c'])
          Confirmepassword=str(request.form['d'])
          for i in range(0,len(username)):
              if username1==username[i] and oldpassword==password[i]:
                 if newpassword==Confirmepassword:
                    password[i]=newpassword 
                    conn = sqlite3.connect("passwd.db")
                    cursor = conn.cursor()
                    sql ="UPDATE user SET password ='%s' WHERE password ='%s'" % (newpassword,oldpassword)
                    cursor.execute(sql)
                    conn.commit()
                    conn.close()
                    return "修改密碼成功"
       return doc
