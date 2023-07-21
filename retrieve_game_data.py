import sqlite3
import json

# Connect đến DB, nếu chưa có DB nào tên như này thì sẽ create
conn = sqlite3.connect('SOVDB.sqlite')
# #Cursor - Na ná như file handle nhưng mà cho DB. File handle cho ta read/write/append file tùy ý, còn cursor cho ta gửi commands nhận responses từ DB.
cur = conn.cursor()

# Đoạn này quá trực quan, đọc là hiểu
cur.executescript('''
            
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Platform;
DROP TABLE IF EXISTS Company;
DROP TABLE IF EXISTS Game;

CREATE TABLE "Genre" (
	"id"	INTEGER NOT NULL PRIMARY KEY UNIQUE,
	"genre"	TEXT UNIQUE
);

CREATE TABLE "Platform" (
	"id"	INTEGER NOT NULL PRIMARY KEY UNIQUE,
	"platform"	TEXT UNIQUE
);
            
CREATE TABLE "Company" (
	"id"	INTEGER NOT NULL PRIMARY KEY UNIQUE,
	"company"	TEXT UNIQUE
);
            
CREATE TABLE "Game" (
	"id"	INTEGER NOT NULL PRIMARY KEY UNIQUE,
	"title"	TEXT,
	"description"	TEXT,
	"publisher"	INTEGER,
	"developer"	INTEGER,
	"genre"	INTEGER,
	"platform"	INTEGER,
	"release_date"	TEXT,
	FOREIGN KEY("platform") REFERENCES "Platform"("id"),
	FOREIGN KEY("publisher") REFERENCES "Company"("id"),
	FOREIGN KEY("developer") REFERENCES "Company"("id"),
	FOREIGN KEY("genre") REFERENCES "Genre"("id")
);
''')

fname = input('Enter file name:')
if (len(fname) < 1): fname = 'games.json' # All game data on freetogame.com
fh = open(fname)
js = json.load(fh)
count = 0
for line in js:
    title = line['title']
    description = line['short_description']
    genre = line['genre']
    platform = line['platform']
    publisher = line['publisher']
    developer = line['developer']
    release_date = line['release_date']
    print(title, description, genre, platform, publisher, developer, release_date)
    # Để placeholder ? rồi truyền input vào trong 1 tuple thay vì viết hẳn input trong câu SQL -> 1. Tránh SQL injection, vì DB sẽ treat input như data thay vì executable code, 2. Performance, vì DB sẽ cache 
    cur.execute('''INSERT OR IGNORE INTO Genre (genre) 
        VALUES ( ? )''', ( genre, ) ) # Chưa có artist này thì nhét vào, có rồi thì thôi. Phải thêm ignore vì ta để id trong bảng Genre là unique.
    cur.execute('SELECT id FROM Genre WHERE genre = ? ', (genre, ) ) #Query ID của genre vừa nhét ở trên
    genre_id = cur.fetchone()[0] #.fetchone() trả record đầu của query results ra ở dạng tuple, thêm [0] để lấy key đầu tiên của tuple đó (id)
    
    cur.execute('''INSERT OR IGNORE INTO Company (company) 
        VALUES ( ? )''', ( publisher, ) )
    cur.execute('SELECT id FROM Company WHERE company = ? ', ( publisher, ) )
    publisher_id = cur.fetchone()[0] # Lấy publisher_id để nhét vào bảng Game
    
    cur.execute('''INSERT OR IGNORE INTO Company (company) 
        VALUES ( ? )''', ( developer, ) )
    cur.execute('SELECT id FROM Company WHERE company = ? ', ( developer, ) )
    developer_id = cur.fetchone()[0] # Lấy developer_id để nhét vào bảng Game

    cur.execute('''INSERT OR IGNORE INTO Game
        (title, description, publisher, developer, genre, release_date) 
        VALUES ( ?, ?, ?, ?, ?, ?, ? )''', ( title, description, publisher_id, developer_id, genre_id, release_date ) )
    cur.execute('SELECT id FROM Game WHERE title = ? ', ( title, ) )
    game_id = cur.fetchone()[0] # Lấy game_id để nhét vào bảng Version
    
    no_of_platform = len(platform.split(","))
    if no_of_platform > 1:
        platforms = line['platform'].split(",")
        for platform in platforms:
            cur.execute('''INSERT OR IGNORE INTO Platform (platform) VALUES ( ? )''', ( platform, ) )
            cur.execute('SELECT id FROM Platform WHERE platform = ? ', ( platform, ) )
            platform_id = cur.fetchone()[0] # Lấy platform_id để nhét vào bảng Version
    else:
            cur.execute('''INSERT OR IGNORE INTO Platform (platform) VALUES ( ? )''', ( platform, ) )
            cur.execute('SELECT id FROM Platform WHERE platform = ? ', ( platform, ) )
            platform_id = cur.fetchone()[0] # Lấy platform_id để nhét vào bảng Version
            
    count += 1
conn.commit()
print(count)

#To do: Tạo 1 bảng Version với 2 cột: game_id, platform_id để thể hiện many-to-many rela.