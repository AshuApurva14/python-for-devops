"""
How to use HTTPResponse and HTTPMessage?

"""

from urllib.request import urlopen
from pprint import pprint           # Use to print data structure in more formated way

with urlopen("https://www.google.com") as response:
    pprint(dir(response))

