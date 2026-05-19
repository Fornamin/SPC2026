import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()

cur.execute('SELECT COUNT(*) FROM users')
count = cur.fetchone()[0]

if count == 0:
    cur.execute('''
        INSERT INTO users (name, age) VALUES (?, ?)
    ''', ('Alice', 30))
    cur.execute('''
        INSERT INTO users (name, age) VALUES ('Amy', 20)
    ''')
    cur.execute('''
        INSERT INTO users (name, age) VALUES ('Elen', 23)
    ''')
else:
    print('Data exists')

conn.commit()
conn.close()