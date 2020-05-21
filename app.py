# flask는 문법이 간단해서 많이 쓰임
# production level에서는 쓰이기 어렵다.
# 확장성에 대한 고민, 어느정도 부하를 견디는지
# 해커톤이나 스타트업 단계 스케치 등

from flask import Flask, jsonify, request, render_template, session
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.secret_key = "fintech"
# app.config[secret_key] = "fintech"
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    pw = db.Column(db.String(50))


@app.route("/")
def hello():
    # templates 폴더가 필요함
    return render_template("hello.html")


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        # 값이 지저분해서 무엇을 만들려는지 알기 어렵다.
        # 그래서 렌더링을 할 것. 렌더 템플릿
        return render_template("signup.html")
        # return """
        # <form action='/signup' method='post'>
        # <p>ID</p><input name='user-id' type='text'>
        # <p>PW</p><input name='user-pw' type='password'>
        # <input type='submit' value='submit'>
        # </form>
        # """

    else:
        form_dict = request.form.to_dict(flat=True)
        user = Users(id=form_dict['user-id'], pw=form_dict['user-pw'])
        db.session.add(user)
        db.session.commit()

        return render_template('welcome.html', user=form_dict['user-id'])


@app.route("/signin", methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        if 'user-id' in session.keys():
            return render_template("welcome.html", user=session['user-id'])
        else:
            return render_template("signin.html")

    else:
        form_dict = request.form.to_dict(flat=True)
        user = Users.query.filter_by(id=form_dict['user-id']).first()
        if user != None and user.pw == form_dict["user-pw"]:
            session['user-id'] = user.id
            return render_template("welcome.html", user=user.id)
        return "id나 비밀번호가 틀립니다"


with open("stocklist.json", "r") as JSON:
    myJSON = json.load(JSON)

"""
# rank 순으로 정렬
mySort = []
for k in myJSON.key():
    mySort.append([k, myJSON[k]["rank"]])
    # 람다?
    mySort.sort(key=lambda x: x[1])
    print(mySort)
"""


@app.route("/stock")
def main():  # 다른 함수 이름과 중복만 안되면 됌
    return jsonify(myJSON)


"""
@app.route("/<int:num>")
def myNum(num):
    myDan = ""
    for i in range(1, 10):
        myDan += "%d * %d = %d</br>" % (num, i, num*i)
    # 웹사이트에서는 스트링만 표현 가능하기 때문에 바로 정수형 넣으면 에러
    return myDan
"""

if __name__ == "__main__":
    app.run(host="localhost", port="5000", debug=True)
