from pykrx import stock
import json
# 회사 이름에 대응되는 ticker라는 것이 있는데 그걸 받아온다
tickers = stock.get_market_ticker_list()
# print(tickers)

myJSON = {}
for ticker in tickers:
    myJSON[ticker] = stock.get_market_ticker_name(ticker)

# name = stock.get_market_ticker_name("000540")

with open("tickerlist.json", "w") as JSON:
    json.dump(myJSON, JSON, ensure_ascii=False)

# with open("tickerlist.json", "r") as JSON:
#     myJSON = json.load(JSON)

print(myJSON)


ohlcv = stock.get_market_ohlcv_by_date("20200501", "20200510", "000660")
print(ohlcv)


df = stock.get_market_price_change_by_ticker("20200501", "20200510")
print(df)
