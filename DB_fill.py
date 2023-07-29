import sqlite3
from API_call import js
from SQL_script import script
# import json

# Connect to an existing DB, or create a brand new DB
conn = sqlite3.connect('game.sqlite')
# Create a DB cursor to interact with the DB. A cursor to a DB is pretty similar to a file handle to a file
cur = conn.cursor()

# Run the script to create the tables
cur.executescript(script)

# In case you can't connect to the API, run the next 4 lines to insert data from games.json to DB instead: 
# fname = input('Enter file name:')
# if (len(fname) < 1): fname = 'non_executable/games.json'
# fh = open(fname)
# js = json.load(fh)

# Transform retrieved Platform data into a list of platforms
def plat_mod(platforms):
    plat_list = [platform.strip() for platform in platforms.split(",")]
    return plat_list

# Extract data of each game
for game in js:
    try:
        title = game['title'].strip()
        description = game['short_description'].strip()
        genre = game['genre'].strip()
        all_platforms = game['platform']
        publisher = game['publisher'].strip()
        developer = game['developer'].strip()
        release_date = game['release_date'].strip()
        # Strip whitespaces for all info, just to be sure.
        print(title, description, genre, all_platforms, publisher, developer, release_date)
    except:
        print("Some info is missing!")
        break

    # Insert extracted 'genre' to table Genre
    cur.execute('''INSERT OR IGNORE INTO Genre (genre) 
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE genre = ? ', (genre, ) ) # Query for genry_ID of the added 'genre'
    genre_id = cur.fetchone()[0] # .fetchone() will output the first row of your result set in a tuple, with 'id' as its 1st element
    
    # Insert extracted 'publisher' to table Company
    cur.execute('''INSERT OR IGNORE INTO Company (company) 
        VALUES ( ? )''', ( publisher, ) )
    cur.execute('SELECT id FROM Company WHERE company = ? ', ( publisher, ) ) # Repeating the process above
    publisher_id = cur.fetchone()[0]
    
    # Insert extracted 'developer' to table Company
    cur.execute('''INSERT OR IGNORE INTO Company (company) 
        VALUES ( ? )''', ( developer, ) )
    cur.execute('SELECT id FROM Company WHERE company = ? ', ( developer, ) ) # Repeating the process above
    developer_id = cur.fetchone()[0]

    # Insert extracted game info to table Game
    cur.execute('''INSERT OR IGNORE INTO Game
        (title, description, publisher_id, developer_id, genre_id, release_date) 
        VALUES ( ?, ?, ?, ?, ?, ?)''', ( title, description, publisher_id, developer_id, genre_id, release_date ) )
    cur.execute('SELECT id FROM Game WHERE title = ? ', ( title, ) ) # Repeating the process above
    game_id = cur.fetchone()[0]
    
    # Transforming all_platforms into a list, since some games are available on multiple platforms
    for platform in plat_mod(all_platforms):
        cur.execute('''INSERT OR IGNORE INTO Platform (platform) VALUES ( ? )''', ( platform, ) )
        cur.execute('SELECT id FROM Platform WHERE platform = ? ', ( platform, ) )
        platform_id = cur.fetchone()[0]
        cur.execute('''INSERT OR IGNORE INTO Version (game_id, platform_id)
        VALUES ( ?, ?)''', ( game_id, platform_id ) )
        # Each pair of game_id and platform_id is a version of the game (e.g. PC version, Xbox version, etc.)
    
print("Success, DB is filled with data!")
conn.commit()

# Close cursor & connection to free memory resources
cur.close()
conn.close()