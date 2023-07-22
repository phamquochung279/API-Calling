import sqlite3
import pandas as pd

conn = sqlite3.connect('game_DB.sqlite')
cur = conn.cursor()
cur.execute('''SELECT * FROM Game WHERE publisher = 10''')
results = cur.fetchall()

print(results)

df = pd.DataFrame()
for x in results:
    df2 = pd.DataFrame(list(x)).T
    df = pd.concat([df, df2])

df.to_html('index.html') # Tự động generate file HTML để show query results