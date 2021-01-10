import sqlite3
import csv
from flask import Flask
conn = sqlite3.connect('1221.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS "Colleges"(
              year INTEGER NOT NULL,
              "schoolId" TEXT NOT NULL,
              "schoolName" TEXT NOT NULL,
              "dayNight" TEXT,
              "level" TEXT,
              "total" INTEGER,
              "m" INTEGER,
              "f" INTEGER,
              "m1" INTEGER,
              "f1" INTEGER,
              "m2" INTEGER,
              "f2" INTEGER,
              "m3" INTEGER,
              "f3" INTEGER,
              "m4" INTEGER,
              "f4" INTEGER,
              "m5" INTEGER,
              "f5" INTEGER,
              "m6" INTEGER,
              "f6" INTEGER,
              "m7" INTEGER,
              "f7" INTEGER,
              "mDelay" INTEGER,
              "fDelay" INTEGER,
              "city" TEXT,
              "system" TEXT
            );''')
conn.commit()

c.execute("delete from Colleges")
conn.commit()

filenames = ['103.csv','104.csv','105.csv','106.csv','107.csv','108.csv']

for file in filenames:
    year = file.split('.')
    with open(file, newline='') as csvfile:

      # 讀取 CSV 檔案內容
      rows = csv.DictReader(csvfile)
      for row in rows:
        sum = int(row['一年級男生']) + int(row['一年級女生']) + int(row['二年級男生'])+ int(row['二年級女生'])+ int(row['三年級男生']) + int(row['三年級女生']) + int(row['四年級男生']) + int(row['四年級女生'])+ int(row['五年級男生']) + int(row['五年級女生']) + int(row['六年級男生']) + int(row['六年級女生'])+ int(row['七年級男生']) + int(row['七年級女生']) + int(row['延修生男生'])+ int(row['延修生女生'])

        m = int(row['一年級男生']) + int(row['二年級男生'])+ int(row['三年級男生']) + int(row['四年級男生'])+ int(row['五年級男生']) + int(row['六年級男生'])  + int(row['七年級男生']) + int(row['延修生男生'])

        f= int(row['一年級女生']) + int(row['二年級女生'])+ int(row['三年級女生']) + int(row['四年級女生'])+int(row['五年級女生']) + int(row['六年級女生']) + int(row['七年級女生']) + int(row['延修生女生'])
        c.execute("INSERT INTO Colleges VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                      (year[0],
                       row['學校代碼'],
                       row['學校名稱'],
                       row['日間∕進修別'],
                       row['等級別'],
                       sum,
                       m,
                       f,
                       int(row['一年級男生']),
                       int(row['一年級女生']),
                       int(row['二年級男生']),
                       int(row['二年級女生']),
                       int(row['三年級男生']),
                       int(row['三年級女生']),
                       int(row['四年級男生']),
                       int(row['四年級女生']),
                       int(row['五年級男生']),
                       int(row['五年級女生']),
                       int(row['六年級男生']),
                       int(row['六年級女生']),
                       int(row['七年級男生']),
                       int(row['七年級女生']),
                       int(row['延修生男生']),
                       int(row['延修生女生']),
                       row['縣市名稱'],
                       row['體系別'],
                       )
                       )

        conn.commit()

print("success")

c.execute("SELECT year, SUM(total) FROM Colleges WHERE level='M 碩士' AND dayNight='D 日' GROUP BY year")
kk=""
for row in c.fetchall():
    year, sum2 =row
    kk=kk+str(year)+' | ' +str(sum2) +'<br>'

conn.commit()

conn.close()

app = Flask(__name__)

@app.route('/')
def index():
    doc='''近六年,全國日間部碩士班總人數變化<br>
{}'''.format(kk)
    return doc;   
