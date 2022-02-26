import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

# ? acts as a placeholder.
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', 
    ('Thunderstruck', 20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', 
    ('My Way', 15))
# input example
title = input("Title? (string) >")
plays = input("Plays? (int) >")
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
    (title, plays))
conn.commit()  # Not so sure what commit does...
# My guess is that it works as git commit. It "sends" the changes to the table
# "Forces data to be written to the database file"

print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
    # rows are returned as tuples, BECAUSE THAT'S WHAT THEY ARE!
    print(row)

cur.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()
# Commit = saves changes!

cur.close()

