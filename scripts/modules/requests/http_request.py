"""
requests modulde in python for performing http requests
"""
# Import the module
import requests

# Define a variable `url` with valid value
url = 'https://api.github.com/invalid'

# Create a Variable called `response` to store the get requests response
response = requests.get(url)

# add if else condition
if response.status_code == 200:
    print('Success')
elif response.status_code == 404:
    print(f"{url} response is {response.status_code}")