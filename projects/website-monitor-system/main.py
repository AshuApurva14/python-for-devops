import requests
import time
import logging
from requests.exceptions import HTTPError

# List of Websites


# Check the HTTP response
def check_website_response(URLS):
    print(f"Monitoring Started for {URLS} ...., Please Wait!")

    for url in URLS:
        try:

           response = requests.get(url)
           response.raise_for_status()

        except HTTPError as http_err:
            print(f"HTTP Error Occurred: {http_err}")
        except Exception as err:
            print(f"Other Error Occured: {err}")

        else:
            print(f"This website {url} is Healthy and response time is: {response.elapsed.total_seconds()}")



URLS = ["https://www.google.com", "https://api.github.com"]

if __name__ == "__main__":
    check_website_response(URLS)
    
