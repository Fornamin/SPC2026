import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()

cur.execute('''
    INSERT INTO users (name, age) VALUES ('Bob', 25)
''')
cur.execute('''
    INSERT INTO users (name, age) VALUES ('Amy', 20)
''')
cur.execute('''
    INSERT INTO users (name, age) VALUES ('Elen', 23)
''')

conn.commit()
conn.close()