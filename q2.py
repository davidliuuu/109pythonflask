from flask import Flask,request
import sqlite3
app = Flask(__name__)

@app.route('/')
def main():

    s='''1. 我在講話的時候，有很多素材和詞彙可講。		
2. 我講話簡潔明瞭，重點突出。	
3. 我善於與和我性格不同的人溝通。	
4. 我對連續不斷的交談感到很容易。	
5. 我可以輕易地向別人描述一件事情。		
6. 跨部門溝通我而言是一件很容易的事情。		
7. 我喜歡和別人聊天。		
8. 和重要的人物（例如上司）談話時，我感到很自然、放鬆。		
9. 我在當眾講話時思維清晰、連貫。
10. 每當面對即興談話，我可以隨時取得素材進行談話。
11. 我喜歡在大庭廣眾之下講話。
12. 我善於跟內向的朋友輕鬆自如地談論自己的情況。
13. 我善於說服人，儘管有時我覺得自己毫無道理。
14. 我善於讚美別人，覺得讚美別人是一件很開心的事情。
15. 講一個完整的故事對我來說很容易。'''

    a=s.split('\n')

    html = '''<head>
<meta charset="utf-8" />
<title> 表達力測試 </title>
</head>

<H1> 表達力測試 </H1>
<p>不要經過思考,只需要根據你的第一反應,選擇最符合的答案.</p>

<form method='POST' action=analyze>
<table>'''

    b=["非常符合","比較符合","不太確定","比較不符合","非常不符合"]
    c=[7,5,3,1,0]
    for i in range(0,15):
        html += '''<tr><td><label for="q{}">{}</label><td>
                   <td>'''.format(i+1,a[i])
        for j in range(0,5):
            html +='''<input id="q{}-{}" name="q{}" type="radio" value={}><label for="q{}-{}">{}</label>'''.format(i+1,j,i+1,c[j],i+1,j,b[j])

        html += '''</td></tr>'''
    html+=''' <TR><TD></TD><TD> <input id="submit" name="submit" type="submit" value="測試結果分析"> </TD></TR></table>
</form>''' 
    

    return html 

@app.route('/analyze',methods=['GET','POST'])
def analyze():
    count =0
    for i in range(15):
        key = 'q{}'.format(i+1) 
        if key in request.values:
           n=int(request.values[key])
           count=count+n
    html = '''<h1>測試結果分析</h1>

<UL>
    <LI> 非常符合 7 分 </LI>
    <LI> 比較符合 5 分 </LI>
    <LI> 不太確定 3 分 </LI>
    <LI> 比較不符合 1 分 </LI>
    <LI> 非常不符合 0 分 </LI>
</UL>

<p>您的總分是 {} </p> 
<table border>
'''.format(count)
    if count<=15:
       html+='''    <tr style='background-color: pink'>td> 0~15 </td> <td> 你的口語表達能力很差，需要針對性地重點提高，除了閱讀本章內容之外，你還需要多花時間去練習書中的公式。假以時日，你的口語表達能力會有很大的提升。 </td></tr>

    <tr ><td> 16~45分 </td> <td> 你的口語表達能力一般，你需要在表達的某些方面進行提升。本章的內容將會對你有很大的幫助。 </td></tr>

    <tr ><td> 46~80分 </td> <td> 你的口語表達能力較好，口語表達對你來說不是難事。但如果你繼續閱讀本章的內容，相信會有錦上添花的作用。 </td></tr>

    <tr ><td> 81~105分 </td> <td> 你的口試表達能力非常好，你已經是講話的高手。如果你不願意花時間在這裡，可以跳到下一章。 </td></tr>

</table>'''
    elif count>15 and count<=45:
         html+='''    <tr ><td> 0~15 </td> <td> 你的口語表達能力很差，需要針對性地重點提高，除了閱讀本章內容之外，你還需要多花時間去練習書中的公式。假以時日，你的口語表達能力會有很大的提升。 </td></tr>

    <tr style='background-color: pink'><td> 16~45分 </td> <td> 你的口語表達能力一般，你需要在表達的某些方面進行提升。本章的內容將會對你有很大的幫助。 </td></tr>

    <tr ><td> 46~80分 </td> <td> 你的口語表達能力較好，口語表達對你來說不是難事。但如果你繼續閱讀本章的內容，相信會有錦上添花的作用。 </td></tr>

    <tr ><td> 81~105分 </td> <td> 你的口試表達能力非常好，你已經是講話的高手。如果你不願意花時間在這裡，可以跳到下一章。 </td></tr>

</table>'''
    elif count>45 and count<=80:
         html+='''    <tr ><td> 0~15 </td> <td> 你的口語表達能力很差，需要針對性地重點提高，除了閱讀本章內容之外，你還需要多花時間去練習書中的公式。假以時日，你的口語表達能力會有很大的提升。 </td></tr>

    <tr ><td> 16~45分 </td> <td> 你的口語表達能力一般，你需要在表達的某些方面進行提升。本章的內容將會對你有很大的幫助。 </td></tr>

    <tr style='background-color: pink'><td> 46~80分 </td> <td> 你的口語表達能力較好，口語表達對你來說不是難事。但如果你繼續閱讀本章的內容，相信會有錦上添花的作用。 </td></tr>

    <tr ><td> 81~105分 </td> <td> 你的口試表達能力非常好，你已經是講話的高手。如果你不願意花時間在這裡，可以跳到下一章。 </td></tr>

</table>'''  
    else:
        html+='''    <tr ><td> 0~15 </td> <td> 你的口語表達能力很差，需要針對性地重點提高，除了閱讀本章內容之外，你還需要多花時間去練習書中的公式。假以時日，你的口語表達能力會有很大的提升。 </td></tr>

    <tr ><td> 16~45分 </td> <td> 你的口語表達能力一般，你需要在表達的某些方面進行提升。本章的內容將會對你有很大的幫助。 </td></tr>

    <tr ><td> 46~80分 </td> <td> 你的口語表達能力較好，口語表達對你來說不是難事。但如果你繼續閱讀本章的內容，相信會有錦上添花的作用。 </td></tr>

    <tr style='background-color: pink'><td> 81~105分 </td> <td> 你的口試表達能力非常好，你已經是講話的高手。如果你不願意花時間在這裡，可以跳到下一章。 </td></tr>

</table>'''
    return html
