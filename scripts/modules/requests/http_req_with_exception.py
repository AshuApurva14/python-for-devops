import requests

from requests.exceptions import HTTPError

url_list = ['https://api.github.com/', 'https://api.github.com/invalid']

# Define a for loop and loop throught the list of urls
for url in url_list:
    try:
       response = requests.get(url)

      # if resposne was successfull, no exception will be raised
       response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exeception as err:
        print(f"Other error occurred: {err}")
    else:
        print('Success!')
        


