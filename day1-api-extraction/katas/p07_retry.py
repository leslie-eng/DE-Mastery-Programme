# add retries to fetch_users at most 3 attempts, waiting 1 sec after the first failure
# and 2 seconds after the second, and only for a timeout or connection failure
import requests
import time
from p04_errors import FetchError

TIMEOUT = 10
API_URL = "https://jsonplaceholder.typicode.com/users"
RETRIES = 3

def fetch_users(url: str = API_URL, timeout: float=10.0) -> list[dict]:
    sleep_start = 1
    try:
        while RETRIES >= 0:
            response = requests.get(url=url, timeout=timeout)
            RETRIES-= 1
            time.sleep(sleep_start)
            sleep_start += 1
        
            if response.status_code != 200:
                    return FetchError(f"The status code {response.status_code}")
                        
            if not isinstance(response.json(), dict):
                    return FetchError(f"The response is not valid JSON")
                
            else:
                if not isinstance(response.json(), list):
                    return FetchError(f"expected a list, got {type(response).__name__}")
                else:
                    return response.json()
            
    except requests.exceptions.Timeout as t:
       return  FetchError(f"The connection timed out {timeout}")
    
    except requests.RequestException as c:
       return  FetchError(f"Could not connect to {API_URL}")
    
    