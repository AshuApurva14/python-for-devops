"""


"""

from urllib.request import urlopen
from pprint import pprint

with  urlopen("https://www.google.com") as response:
      pass

pprint(response.headers.items())

pprint(response.getheader("Server"))

pprint(response.headers["Server"])

