# turning library errors into your own, one cause per message, 
# the shape of the Day 1 fetch_users
from p04_errors import FetchError

TIMEOUT = 10
API_URL = "https://jsonplaceholder.typicode.com/users"

import requests
import json



def fetch_users(url: str = API_URL, timeout: float=10.0) -> list[dict]:
    try:
        response = requests.get(url=url, timeout=timeout)
        if response.status_code != 200:
            raise FetchError(f"The status code {response.status_code}")
        
        if not isinstance(response.json(), dict):
            raise FetchError(f"The response is not valid JSON")
        
        else:
            if not isinstance(response.json(), list):
                raise FetchError(f"expected a list, got {type(response).__name__}")
            
            else:
                return response.json()

    except requests.exceptions.Timeout as t:
        return FetchError(f"The connection timed out {timeout}")
    
    except requests.RequestException as c:
        return FetchError(f"Could not connect to {API_URL}")

print(fetch_users(url=API_URL, timeout=0.001))
print(fetch_users(url="https://jsonplaceholder.typicode.invalid/users"))
print(fetch_users(url="https://jsonplaceholder.typicode.com/userz"))
print(fetch_users(url="https://example.com"))
print(fetch_users(url="https://jsonplaceholder.typicode.com/users/1"))      