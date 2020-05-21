from flask import Flask, jsonify, request
import json
# flask는 문법이 간단해서 많이 쓰임
# production level에서는 쓰이기 어렵다.
# 확장성에 대한 고민, 어느정도 부하를 견디는지
# 해커톤이나 스타트업 단계 스케치 등

app = Flask(__name__)


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return """
        <form action='/signup' method='post'>
        <p>ID</p><input name='user-id' type='text'>
        <p>PW</p><input name='user-pw' type='password'>
        <input type='submit' value='submit'>
        </form>
        """
    else:
        return jsonify(request.form.to_dict())


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
