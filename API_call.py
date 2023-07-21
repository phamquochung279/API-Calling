import urllib.request, urllib.parse, urllib.error
import json
import ssl

endpoint = 'https://www.freetogame.com/api/games?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# Gắn API endpoint với query parameters
url = endpoint + urllib.parse.urlencode({'sort-by': "alphabetical"})

print('Retrieving', url)
# Đi đến URL đã tạo & nhét data vào file handle 'uh'
uh = urllib.request.urlopen(url, context=ctx)

# Read trả ra file ở dạng bytes, decode biến file thành Python string - Unicode
data= uh.read().decode()

try:
    # Parse data bằng JSON, nhận về 1 Python list chứa multiple dict (vì freetogame trả ra file JSON dạng array)
    js = json.loads(data)
    # Print ra JSON bản beautified, lề = 4 spaces
    print(json.dumps(js, indent=4))
    # print(type(js))
except:
    js = None
    print("Cannot convert to JSON!")