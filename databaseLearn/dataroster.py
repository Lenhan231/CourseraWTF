import json
import sqlite3

conn = sqlite3.connect('dataroster.sqlite')
cur = conn.cursor()

TableName = ["User", "Course", "Member"]
for name in TableName:
    cur.execute('DROP TABLE IF EXISTS {}'.format(name))

cur.execute('''
CREATE TABLE User (
    id Integer Not Null primary key autoincrement unique,
    name    TEXT UNIQUE
)''')

cur.execute('''
CREATE TABLE Course (
    id Integer Not Null primary key autoincrement unique,
    title    TEXT UNIQUE
)''')

cur.execute('''
CREATE TABLE Member (
    role    INTERGER,
    user_id INTERGER,
    course_id INTERGER
)''')

handle = open('roster_data.json','r')
lines = json.load(handle)

for pieces in lines:
    if len(pieces) < 3 : continue
    name = pieces[0]
    title = pieces[1]
    role = pieces[2]

    cur.execute('''INSERT OR IGNORE INTO User (name)
                VALUES ( ? )''', (name,))
    user_id = cur.lastrowid
    
    cur.execute('''INSERT OR IGNORE INTO Course (title)
                VALUES ( ? )''', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR IGNORE INTO Member (role, user_id, course_id) VALUES (?, ?, ?)''', (role, user_id, course_id))

    conn.commit()
    


