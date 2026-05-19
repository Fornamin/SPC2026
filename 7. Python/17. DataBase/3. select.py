import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()

cur.execute('SELECT * FROM users')

# 데이터가 바뀐 게 없으므로 commit하는 것에 영향 X
# conn.commit()

rows = cur.fetchall()
print(rows)

conn.close()