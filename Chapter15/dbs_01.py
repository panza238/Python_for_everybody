import sqlite3

# Create connection to sqlite DB
conn = sqlite3.connect('music.sqlite')
# conn is an OBJECT that interacts with the database
print(conn)

cur = conn.cursor()  # Cursor is the analogous to a file handle
# it is as if we were calling 'open' on a text file
cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')
conn.close()

# Cursor reads and writes. Interacts with the database. IT IS A HANDLE
