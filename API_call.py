import urllib.request, urllib.parse, urllib.error
import json
import sys

endpoint = 'https://www.freetogame.com/api/games'

# Nối API endpoint với query parameters
url = endpoint + urllib.parse.urlencode({'sort-by': "alphabetical"})

print('Retrieving', url)

# Đi đến URL đã tạo & trả lại http.client.HTTPResponse object - 1 file-like object

uh = urllib.request.urlopen(url)
data = uh.read().decode() # Read đọc file-like objects & trả ra file ở dạng bytes. Decode biến file thành Python string (Unicode)
try:
# Parse data bằng JSON, nhận về 1 Python list chứa multiple dict (vì freetogame trả ra JSON objects trong 1 array)
    js = json.loads(data)
# Print ra JSON bản beautified, lề = 4 spaces
    # print(json.dumps(js, indent=4))
except:
    js = None
    print("Cannot convert to JSON. Curse you freetogame.com!")