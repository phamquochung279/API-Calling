import sqlite3
from API_call import js
# import json

# Connect đến DB, nếu chưa có DB nào tên như này thì sẽ create
conn = sqlite3.connect('game_DB.sqlite')
# Cursor - Na ná như file handle nhưng mà cho DB. File handle cho ta read/write/append file tùy ý, còn cursor cho ta gửi commands nhận responses từ DB.
cur = conn.cursor()

# DROP hết 5 tables nếu muốn restart việc insert data vào DB mỗi lần run script
# cur.executescript('''
            
# DROP TABLE IF EXISTS Genre;
# DROP TABLE IF EXISTS Platform;
# DROP TABLE IF EXISTS Company;
# DROP TABLE IF EXISTS Game;
# DROP TABLE IF EXISTS Version

# ''')

# Thêm IF NOT EXISTS để không phải tạo lại existing tables.
cur.executescript('''
            
CREATE TABLE IF NOT EXISTS "Genre" (
	"id"	INTEGER NOT NULL PRIMARY KEY UNIQUE,
	"genre"	TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS "Platform" (
	"id"	INTEGER NOT NULL PRIMARY KEY UNIQUE,
	"platform"	TEXT UNIQUE
);
            
CREATE TABLE IF NOT EXISTS "Company" (
	"id"	INTEGER NOT NULL PRIMARY KEY UNIQUE,
	"company"	TEXT UNIQUE
);
            
CREATE TABLE IF NOT EXISTS "Game" (
    "id" INTEGER NOT NULL PRIMARY KEY UNIQUE,
    "title" TEXT,
    "description" TEXT,
    "publisher" INTEGER,
    "developer" INTEGER,
    "genre" INTEGER,
    "release_date" TEXT,
    FOREIGN KEY("publisher") REFERENCES "Company"("id") ON DELETE SET NULL,
    FOREIGN KEY("developer") REFERENCES "Company"("id") ON DELETE SET NULL,
    FOREIGN KEY("genre") REFERENCES "Genre"("id") ON DELETE SET NULL,
    UNIQUE("title", "publisher", "developer", "release_date")
);
                  
CREATE TABLE IF NOT EXISTS "Version" (
	"game_id"	INTEGER,
	"platform_id"	INTEGER,
	FOREIGN KEY("platform_id") REFERENCES "Platform"("id") ON DELETE SET NULL,
	FOREIGN KEY("game_id") REFERENCES "Game"("id") ON DELETE CASCADE,
	PRIMARY KEY("game_id","platform_id")
)
''')

# Chạy 4 dòng dưới nếu có vấn đề connection khi call API:
# fname = input('Enter file name:')
# if (len(fname) < 1): fname = 'games.json'
# fh = open(fname)
# js = json.load(fh)

def plat_mod(a):
    a = a.split(",")
    for b in a:
        a[a.index(b)] = b.strip()
    return a

for line in js:
    try:
        title = line['title'].strip()
        description = line['short_description'].strip()
        genre = line['genre'].strip()
        all_platforms = line['platform'].strip()
        publisher = line['publisher'].strip()
        developer = line['developer'].strip()
        release_date = line['release_date'].strip()
        print(title, description, genre, all_platforms, publisher, developer, release_date)
    except:
        print("Some info is missing!")
    # Để placeholder ? rồi truyền input vào trong 1 tuple thay vì viết hẳn input trong câu SQL -> 1. Tránh SQL injection, vì DB sẽ treat input như data thay vì executable code, 2. Performance, vì DB sẽ cache.
    
    # Nhét genre vào bảng Genre
    cur.execute('''INSERT OR IGNORE INTO Genre (genre) 
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE genre = ? ', (genre, ) ) #Query ID của genre vừa nhét ở trên
    genre_id = cur.fetchone()[0] #.fetchone() trả record đầu của query results ra ở dạng tuple, thêm [0] để lấy key đầu tiên của tuple đó (id)
    
    # Nhét tên của publishing company vào bảng Company
    cur.execute('''INSERT OR IGNORE INTO Company (company) 
        VALUES ( ? )''', ( publisher, ) )
    cur.execute('SELECT id FROM Company WHERE company = ? ', ( publisher, ) )
    publisher_id = cur.fetchone()[0] # Lấy publisher_id để nhét vào bảng Game
    
    # Nhét tên của development company vào bảng Company
    cur.execute('''INSERT OR IGNORE INTO Company (company) 
        VALUES ( ? )''', ( developer, ) )
    cur.execute('SELECT id FROM Company WHERE company = ? ', ( developer, ) )
    developer_id = cur.fetchone()[0] # Lấy publisher_id để nhét vào bảng Game

    # Nhét data của game (trừ platform) vào bảng Game.
    cur.execute('''INSERT OR IGNORE INTO Game
        (title, description, publisher, developer, genre, release_date) 
        VALUES ( ?, ?, ?, ?, ?, ?)''', ( title, description, publisher_id, developer_id, genre_id, release_date ) )
    cur.execute('SELECT id FROM Game WHERE title = ? ', ( title, ) )
    game_id = cur.fetchone()[0] # Lấy game_id để nhét vào bảng Version
    
    # Biến all_platforms thành 1 list các platform, nhét từng element của list cùng với game_id vào bảng Version
    for platform in plat_mod(all_platforms):
        cur.execute('''INSERT OR IGNORE INTO Platform (platform) VALUES ( ? )''', ( platform, ) )
        cur.execute('SELECT id FROM Platform WHERE platform = ? ', ( platform, ) )
        platform_id = cur.fetchone()[0] # Lấy platform_id để nhét vào bảng Version
        cur.execute('''INSERT OR IGNORE INTO Version (game_id, platform_id)
        VALUES ( ?, ?)''', ( game_id, platform_id ) ) # Nhét 1 cặp game_id & platform_id vào bảng Version
    
conn.commit()

# Close cursor và connection để free resources
cur.close()
conn.close()

# Total: 407 coms, 379 games, 15 genres, 2 platforms, 388 versions