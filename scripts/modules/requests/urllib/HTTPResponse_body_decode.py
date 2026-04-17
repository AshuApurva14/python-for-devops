from urllib.request import urlopen

with urlopen("https://www.google.com/in") as response:
    body = response.read()

character_set = response.headers.get_content_charset()

content = body.decode(character_set)

with open("google.html", encoding="utf-8", mode="w") as file:
    file.write(content)




