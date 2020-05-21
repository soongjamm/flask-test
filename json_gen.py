# json이라는 파일을 만들고 웹에 노출시켜주기 위한 파일
import json

stock = {
    "skhynix": {
        "price": 9000,
        "rank": 4
    },
    "kisa": {
        "price": 3000,
        "rank": 2
    },
    "samsung": {
        "price": 50000,
        "rank": 3
    }
}

# 파일을 여는 함수. 열것인지, 작성할 것인지
with open("stocklist.json", "w") as JSON:
    json.dump(stock, JSON)

with open("stocklist.json", "r") as JSON:
    myJSON = json.load(JSON)

print(myJSON)
