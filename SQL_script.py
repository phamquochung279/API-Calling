script = '''CREATE TABLE IF NOT EXISTS "Genre" (
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
    "publisher_id" INTEGER,
    "developer_id" INTEGER,
    "genre_id" INTEGER,
    "release_date" TEXT,
    FOREIGN KEY("publisher_id") REFERENCES "Company"("id") ON DELETE SET NULL,
    FOREIGN KEY("developer_id") REFERENCES "Company"("id") ON DELETE SET NULL,
    FOREIGN KEY("genre_id") REFERENCES "Genre"("id") ON DELETE SET NULL,
    UNIQUE("title", "publisher_id", "developer_id", "release_date")
);
                  
CREATE TABLE IF NOT EXISTS "Version" (
	"game_id"	INTEGER,
	"platform_id"	INTEGER,
	FOREIGN KEY("platform_id") REFERENCES "Platform"("id") ON DELETE SET NULL,
	FOREIGN KEY("game_id") REFERENCES "Game"("id") ON DELETE CASCADE,
	PRIMARY KEY("game_id","platform_id")
)'''

# Add these lines to the start of 'script' if you want to reset data in DB each time DB_fill.py is run:

# DROP TABLE IF EXISTS Genre;
# DROP TABLE IF EXISTS Platform;
# DROP TABLE IF EXISTS Company;
# DROP TABLE IF EXISTS Game;
# DROP TABLE IF EXISTS Version