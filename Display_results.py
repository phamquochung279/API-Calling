import sqlite3

# Check xem query có phải SELECT không, hay là command phá hoại 
banned_statements = ['INSERT', 'UPDATE', 'DELETE', 'CREATE', 'ALTER', 'DROP']

def query_check(a):
    for statement in banned_statements:
        if statement in a.upper():
            return True
    return False

while True:
    try:
        conn = sqlite3.connect('file:game.sqlite?mode=ro', uri=True)
        cursor = conn.cursor()
    except:
        print("DB doesn't exist!")
        break

    query = input('Enter your SQL query:')
    # E.g. SELECT * FROM Game WHERE publisher = 6
    
    if query_check(query) is True:
        print("Bro! Don't mess with my DB.")
        continue

    print("Executing...")
    try:
        cursor.execute(query)
    except:
        print("Invalid query! Do you even know SQL bro?") # E.g. SELECT abcdefgh
        continue

    # cursor.description trả ra 1 tuple các info của các cột trong query results, trong đó element đầu của tuple là tên cột.
    column_names = [description[0] for description in cursor.description]

    # fetchall() lấy toàn bộ query results
    rows = cursor.fetchall()

    if len(rows) == 0: # E.g. SELECT * FROM Game WHERE publisher = 14
        print('No results. How about another query?')
        continue

    print(rows)

    HTML_file = input("Query completed! Name an HTML file to show your results (no .html extension):")
    #E.g. output

    # Tạo mới/mở file output.html (nếu đã có). 'w' - writing - để overwrite nội dung đang có trong file
    with open(f'{HTML_file}.html', 'w') as file:
        # Viết sẵn head, title, link đến styles trong file styles.css. Mở sẵn html, body, table tag để chuẩn bị insert query results
        file.write('<!DOCTYPE html>\n<html>\n<head>\n<title>Query Results</title>\n<link rel="stylesheet" type="text/css" href="styles.css">\n</head>\n<body>\n<table>')

        # Tạo row đầu tiên của table để chuẩn bị chứa các tên cột
        file.write('<tr>\n')
        for column_name in column_names:
            file.write(f'<th>{column_name}</th>\n') # Viết các tag <th> - header cell - để chứa tên cột
        file.write('</tr>\n')

        # fetchall() trả ra 1 list các tuple, mỗi tuple chứa các value của mỗi row trong result set.
        for row in rows: # for loop qua từng tuple (row)
            file.write('<tr>\n')
            for value in row: # for loop qua từng value của tuple (row)
                file.write(f'<td>{value}</td>\n') # Viết các tag <td> - data cell - chứa các value của dòng
            file.write('</tr>\n')

        # Đóng tag table, body và html
        file.write('</table>\n')
        file.write('</body>\n</html>\n')

    print(f"Done! Open {HTML_file}.html on a browser to see your results.")

    # Đóng cursor & connection để free memory resources
    cursor.close()
    conn.close()
    break
