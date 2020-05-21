import sqlite3

conn = sqlite3.connect("db.sqlite3")
cur = conn.cursor()
res = cur.execute("SELECT * FROM Users").fetchall
print("------")
print(res)
