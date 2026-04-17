from urllib.request import urlopen

with urlopen("https://www.google.com") as response:  # create a context
    body = response.read()

with open("example.html", mode="wb") as html_file:
    html_file.write(body)