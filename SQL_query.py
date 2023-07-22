import sqlite3
import pandas as pd

conn = sqlite3.connect('game_DB.sqlite')
cur = conn.cursor()

query = input('Enter your SQL query:')
# E.g. SELECT * FROM Game WHERE publisher = 10

cur.execute(query)
results = cur.fetchall()

print(results)

df = pd.DataFrame()
for x in results:
    df2 = pd.DataFrame(list(x)).T
    df = pd.concat([df, df2])

# Append the HTML to the existing 'template.html' file
with open('results.html', 'a') as file:
    file.write('''<!DOCTYPE html>
<html>
<head>
    <title>SQLite Query Results</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>''')
    df.to_html(file, index=False)
    file.write('''</body>
               </html>''')