import sqlite3

conn = sqlite3.connect('Test.db')
curs = conn.cursor()

conn.execute('''create table items
  (id integer primary key, X integer, Y integer)''')

conn.execute("INSERT INTO items (X, Y) VALUES (25, 34)")

conn.commit()