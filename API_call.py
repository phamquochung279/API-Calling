from urllib import request, parse
import json
import ssl

# Ignore SSL certificate errors (if any)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

endpoint = 'https://www.freetogame.com/api/games?'

# Concatenating endpoint & query parameters to create API URL
url = endpoint + parse.urlencode({'sort-by': "alphabetical"})

print('Retrieving', url)

uh = request.urlopen(url, context=ctx) # Sending GET request to API & get http.client.HTTPResponse object

data = uh.read().decode() # read() converts object into bytes, decode() converts the bytes into a Python string

try:
# Parsing JSON data
    js = json.loads(data)
# Print beautified version of parsed data
    print(json.dumps(js, indent=4))
    print("JSON successfully retrived & parsed!")
except:
    js = None
    print("Cannot convert to JSON!")