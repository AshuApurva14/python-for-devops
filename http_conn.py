"""
HTTP module for web request

"""

import requests
response = requests.get("https://api.github.com")

if response.status_code == 200:
    print("success!")
elif response.status_code == 404:
    print("Not Found!")



