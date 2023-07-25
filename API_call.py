from urllib import request, parse
import json

endpoint = 'https://www.freetogame.com/api/games?'

# Nối API endpoint với query parameters
url = endpoint + parse.urlencode({'sort-by': "alphabetical"})

print('Retrieving', url)

# Đi đến URL đã tạo & trả lại http.client.HTTPResponse object

uh = request.urlopen(url)
data = uh.read().decode() # Read đọc http.client.HTTPResponse object & trả ra file ở dạng bytes. Decode biến bytes thành Python string (Unicode)
try:
# Parse data bằng JSON, nhận về 1 Python list chứa multiple dict (vì freetogame trả ra JSON objects trong 1 array)
    js = json.loads(data)
# Print ra JSON bản beautified, lề = 4 spaces
    print(json.dumps(js, indent=4))
    print("JSON successfully retrived & parsed!")
except:
    js = None
    print("Cannot convert to JSON!")