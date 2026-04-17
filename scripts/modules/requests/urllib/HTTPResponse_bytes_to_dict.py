import json
from urllib.request import urlopen

with urlopen("https://httpbin.org/json") as response:
    body = response.read()

print(type(body))

data = json.loads(body)

print(type(data))
print(data)