import sqlite3

conn = sqlite3.connect('track.sqlite')
cur = conn.cursor()

TableName = ['Artist', 'Genre', 'Album', 'Track']
for Name in TableName:
    cur.execute('DROP TABLE IF EXISTS {}'.format(Name))

cur.execute('''
CREATE TABLE Artist (
    id Integer Not Null primary key autoincrement unique,
    name    TEXT UNIQUE
)''')

cur.execute('''
CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);''')

cur.execute('''
CREATE TABLE Album(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            artist_id INTEGER,
            title TEXT UNIQUE
);''')

cur.execute('''
CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);''')

handle = open('tracks.csv', 'r')
lines = handle.readlines()
for line in lines:
    pieces = line.strip().split(',')
    if len(pieces) < 6 : continue
    name = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]
    GenreName = pieces[6]

    print(name, artist, album, count, rating, length, GenreName)
    cur.execute('''INSERT OR IGNORE INTO Genre (name)
                VALUES ( ? )''', (GenreName,))
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (GenreName, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, genre_id, album_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, genre_id, album_id, length, rating, count ) )
    
    conn.commit()
