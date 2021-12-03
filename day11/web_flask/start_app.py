# 웹 서버 만들기
from flask import Flask, render_template, request

app = Flask(__name__)       #Flask 객체 app 생성

@app.route('/')
#@ - 애너테이션,  '/'루트 경로,  ip - 127.0.0.1:5000 -> host:port
def index():
    return render_template('index.html')    #html 파일을 index에 전송
    #return "<h1>Hello~ Flask!!</h1>"  #문자열을 페이지에 전송


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':        #만약 POST 방식 이라면
        id = request.form['id']             #name값 id를 가져옴
        pwd = request.form['pwd']           #name값 passwd를 가져옴
        name = request.form['name']
        return render_template('member_info.html', id=id, pwd=pwd, name=name)

    else:
        return render_template('register.html')     #GET 방식


@app.route('/loop_index/')
def get_loopindex():
    items = ['a', 'b', 'c', 'd']
    return render_template('loop_index.html', items=items)      # 앞 times가 보내는 애, 뒤는 받는 애??



@app.route('/even_odd/', methods = ['GET', 'POST'])
def even_odd():
    if request.method == "POST":
        try:
        # 데이터 수집
            num = int(request.form['num'])  #문자를 숫자로 바꿈
        except ValueError:
            error_message = "숫자를 입력해주세요"
            return render_template('even_odd.html', error_message=error_message)
        else:
        # 데이터 처리
            if num % 2 == 0:
                result = "짝수입니다."
            else:
                result = "홀수입니다."
            return render_template('calc_result.html', num=num, result=result)
    else: #GET인 경우
        return render_template('even_odd.html')



app.run(debug=True)
#debuf=True 서비스 하기 전 개발 모드