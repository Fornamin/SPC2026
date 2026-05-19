import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()

# 테이블 생성 -> ORM
# class Users:
#     id,
#     name, 
#     age,

# cur.execute(Users)

cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )''')

conn.commit()
conn.close()