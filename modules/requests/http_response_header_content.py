"""
You can access the content of a response in three different ways and formats. Here is a quick overview about the different ways and formats:

  1. content: This attribute returns the raw bytes of the response content
   2.  text: The text attribute returns the content as a normal UTF-8 encoded Python string
    3. json(): You can use the json() method to get the response content in JSON format
"""



import requests

url = 'https://api.github.com/'

response = requests.get(url)

print(response.content)  # Access the content of response

print(response.headers) # Access the response header

print(response.headers['Content-Type'])  # Access the content type of response 