import sqlite3

# Prevent DML/DDL commands
banned_statements = ['INSERT', 'UPDATE', 'DELETE', 'CREATE', 'ALTER', 'DROP', 'TRUNCATE']

def query_check(a):
    for statement in banned_statements:
        if statement in a.upper():
            return True
    return False

while True:
    # Only connects if DB already exists - creating new DB is not allowed
    try:
        conn = sqlite3.connect('file:game.sqlite?mode=ro', uri=True)
        cursor = conn.cursor()
    except:
        print("DB doesn't exist!")
        break

    query = input('Enter your SQL query:')
    # E.g. SELECT * FROM Game WHERE publisher = 6
    
    if query_check(query) is True:
        print("You aren't allowed to make changes to the DB!")
        continue

    print("Executing...")
    try:
        cursor.execute(query)
    except:
        print("Invalid query! Check your syntax.") # E.g. SELECT abcdefgh
        continue

    # cursor.description() outputs tuples of info on result set's columns. Column names are the first elements of said tuples.
    column_names = [description[0] for description in cursor.description]

    # fetchall() returns all resulting rows, or a blank Python list if there is no result.
    rows = cursor.fetchall()

    if len(rows) == 0: # E.g. SELECT * FROM Game WHERE publisher = 14
        print('No results. Anything else you wanna look for?')
        continue

    print(rows)

    HTML_file = input("Query completed! Name an HTML file to see your results (no .html extension):")
    if (len(HTML_file) < 1): HTML_file = 'output'
    # E.g. output

    # Create a new HTML file or open an existing one. Overwrite the file's contents:
    with open(f'{HTML_file}.html', 'w') as file:
        # Compliance with basic HTML file structure...
        file.write('<!DOCTYPE html>\n<html>\n<head>\n<title>Query Results</title>\n<link rel="stylesheet" type="text/css" href="styles.css">\n</head>\n<body>\n<table>')

        # First row of the table shows all column names of the result set
        file.write('<tr>\n')
        for column_name in column_names:
            file.write(f'<th>{column_name}</th>\n')
        file.write('</tr>\n')

        # Loading values of resulting rows into table cells
        for row in rows:
            file.write('<tr>\n')
            for value in row:
                file.write(f'<td>{value}</td>\n')
            file.write('</tr>\n')

        # Finishing up with closing tags
        file.write('</table>\n')
        file.write('</body>\n</html>\n')

    print(f"Done! Open {HTML_file}.html on a browser to see your results.")

    # Closing DB cursor & connection then breaking the while loop, exiting the app
    cursor.close()
    conn.close()
    break
