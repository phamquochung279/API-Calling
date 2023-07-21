import gzip
import urllib.request, urllib.parse, urllib.error
import json
import ssl
import sqlite3

endpoint = 'https://www.freetogame.com/api/games?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# Gắn API endpoint với query parameters
url = endpoint + urllib.parse.urlencode({'sort-by': "alphabetical"})

print('Retrieving', url)
#Đi đến URL đã tạo & nhét data vào file handle 'uh'
uh = urllib.request.urlopen(url, context=ctx).read()
#Read để lấy content toàn bộ file, và decompress file từ gzip ra Unicode
data= uh.decode()

print(data, type(data)) # Nhận 1 string

try:
    #Parse data bằng JSON, nhận về 1 Python list chứa multiple dict (vì freetogame trả ra file JSON dạng array)
    js = json.loads(data)
    print(js)
    print(type(js))
except:
    js = None
    print("shit")

# #Đi về đầu loop -> hỏi lại URL của mình (Enter location:)
# #print(json.dumps(js, indent=4))
# else:
#     place_id = js['results'][0]['place_id']
#     print(place_id)