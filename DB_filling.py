import sqlite3
from API_call import js

# Connect đến DB, nếu chưa có DB nào tên như này thì sẽ create
conn = sqlite3.connect('game_DB.sqlite')
# #Cursor - Na ná như file handle nhưng mà cho DB. File handle cho ta read/write/append file tùy ý, còn cursor cho ta gửi commands nhận responses từ DB.
cur = conn.cursor()

# Đoạn này quá trực quan, đọc là hiểu
cur.executescript('''
            
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Platform;
DROP TABLE IF EXISTS Company;
DROP TABLE IF EXISTS Game;
DROP TABLE IF EXISTS Version;

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
	"release_date"	TEXT,
	FOREIGN KEY("publisher") REFERENCES "Company"("id") ON DELETE SET NULL,
	FOREIGN KEY("developer") REFERENCES "Company"("id") ON DELETE SET NULL,
	FOREIGN KEY("genre") REFERENCES "Genre"("id")
);
                  
CREATE TABLE "Version" (
	"game_id"	INTEGER,
	"platform_id"	INTEGER,
	FOREIGN KEY("platform_id") REFERENCES "Platform"("id") ON DELETE SET NULL,
	FOREIGN KEY("game_id") REFERENCES "Game"("id") ON DELETE CASCADE,
	PRIMARY KEY("game_id","platform_id")
);
''')
# Chạy 4 dòng dưới nếu có vấn đề connection khi call API:
# fname = input('Enter file name:')
# if (len(fname) < 1): fname = 'games.json' # Full data từ freetogame.com - trả khi call endpoint https://www.freetogame.com/api/games
# fh = open(fname)
# js = json.load(fh)

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
    # Để placeholder ? rồi truyền input vào trong 1 tuple thay vì viết hẳn input trong câu SQL -> 1. Tránh SQL injection, vì DB sẽ treat input như data thay vì executable code, 2. Performance, vì DB sẽ cache 
    
    # Nhét data vào bảng Genre
    cur.execute('''INSERT OR IGNORE INTO Genre (genre) 
        VALUES ( ? )''', ( genre, ) ) # Chưa có artist này thì nhét vào, có rồi thì thôi. Phải thêm ignore vì ta để id trong bảng Genre là unique.
    cur.execute('SELECT id FROM Genre WHERE genre = ? ', (genre, ) ) #Query ID của genre vừa nhét ở trên
    genre_id = cur.fetchone()[0] #.fetchone() trả record đầu của query results ra ở dạng tuple, thêm [0] để lấy key đầu tiên của tuple đó (id)
    
    # Nhét data cho publishing company vào bảng Company
    cur.execute('''INSERT OR IGNORE INTO Company (company) 
        VALUES ( ? )''', ( publisher, ) )
    cur.execute('SELECT id FROM Company WHERE company = ? ', ( publisher, ) )
    publisher_id = cur.fetchone()[0] # Lấy publisher_id để nhét vào bảng Game
    
    # Nhét data cho developing company vào bảng Company
    cur.execute('''INSERT OR IGNORE INTO Company (company) 
        VALUES ( ? )''', ( developer, ) )
    cur.execute('SELECT id FROM Company WHERE company = ? ', ( developer, ) )
    developer_id = cur.fetchone()[0] # Lấy developer_id để nhét vào bảng Game

    # Nhét data game (trừ platform) vào bảng Game
    cur.execute('''INSERT OR IGNORE INTO Game
        (title, description, publisher, developer, genre, release_date) 
        VALUES ( ?, ?, ?, ?, ?, ?)''', ( title, description, publisher_id, developer_id, genre_id, release_date ) )
    cur.execute('SELECT id FROM Game WHERE title = ? ', ( title, ) )
    game_id = cur.fetchone()[0] # Lấy game_id để nhét vào bảng Version
    
    # Check xem game available trên mấy platform
    split_platforms = all_platforms.split(",")
    no_of_platform = len(split_platforms)

    # Nếu nhiều hơn 1 platform -> chạy for loop qua từng platform, nhét từng cặp platform & game vào bảng Version.
    if no_of_platform > 1:
        for raw_platform in split_platforms:
            platform = raw_platform.strip()
            cur.execute('''INSERT OR IGNORE INTO Platform (platform) VALUES ( ? )''', ( platform, ) )
            cur.execute('SELECT id FROM Platform WHERE platform = ? ', ( platform, ) )
            platform_id = cur.fetchone()[0] # Lấy platform_id để nhét vào bảng Version
            cur.execute('''INSERT OR IGNORE INTO Version (game_id, platform_id)
            VALUES ( ?, ?)''', ( game_id, platform_id ) ) # Nhét 1 cặp game_id & platform_id vào bảng Version
    
    # Nếu số platform = 1 -> nhét luôn platform & game vào bảng Version.
    elif no_of_platform == 1:
        platform = all_platforms
        cur.execute('''INSERT OR IGNORE INTO Platform (platform) VALUES ( ? )''', ( platform , ) )
        cur.execute('SELECT id FROM Platform WHERE platform = ? ', ( platform , ) )
        platform_id = cur.fetchone()[0] # Lấy platform_id để nhét vào bảng Version
        cur.execute('''INSERT OR IGNORE INTO Version (game_id, platform_id)
        VALUES ( ?, ?)''', ( game_id, platform_id ) )
conn.commit()

# Close cursor và connection để free resources
cur.close()
conn.close()