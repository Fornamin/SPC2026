import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()

cur.execute("UPDATE users SET age = 28 WHERE name = 'Bob'")

conn.commit()
conn.close()