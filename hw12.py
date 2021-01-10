from flask import Flask,request

app = Flask(__name__)
@app.route('/')
def html():
   doc ='''<FORM METHOD=POST ACTION =menu>
Username<INPUT TYPE=TEXT NAME=a><br>
Password<INPUT TYPE=TEXT NAME=b><br>
<INPUT TYPE=SUBMIT>'''
   return doc
@app.route('/menu',methods=['GET','POST'])
def menu():
   username=[]
   password=[]
   a=str(request.form['a'])
   b=str(request.form['b'])
   f = open('passwd.txt','r')
   for line in f.readlines():
     x = line.split(":")
     username.append(x[0])
     y = x[1].split( )
     password.append(y[0])
   f.close()
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
          username=str(request.form['a'])
          oldpassword=str(request.form['b'])
          newpassword=str(request.form['c'])
          Confirmepassword=str(request.form['d'])
          name=username+":"+oldpassword
          f = open('passwd.txt','r')
          for line in f.readlines():
            x = line.split( )
            if name == x[0]:
               f.close()
               f = open("passwd.txt","r+")
               fstring=f.read()
               idfilter=name
               idposition=fstring.find(idfilter)
               f.seek(idposition,0)
               print(newpassword)
               print(Confirmepassword) 
               if newpassword==Confirmepassword:
                  name=username+":"+newpassword 
               print(name)
               f.write(name) 
               f.close()
            return '修改密碼成功'     
          
       return doc
   
