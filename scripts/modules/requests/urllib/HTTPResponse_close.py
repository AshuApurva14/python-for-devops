"""
Decode Bytes Object with `.decode()`
Get Character Set information from headers with `.get_content_charset()`

"""

from urllib.request import urlopen

with urlopen("https://www.google.com") as response:  # create a context
    body = response.read()    # read the response

character_set = response.headers.get_content_charset()

decode_body = body.decode(character_set)
print(decode_body[:60])

