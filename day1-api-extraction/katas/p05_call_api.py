TIMEOUT = 10
API = "https://jsonplaceholder.typicode.com/users"

import requests
import json

# Teaches: requests.get, status codes, .json(), a timeout, reading a real response

try:
    response = requests.get(url=API, timeout=TIMEOUT)
    print("Status:", response.status_code)
    print(f"Users received: {len(response.json())}")
    print(f"Keys: {response.json()[0].keys}")
    
except TimeoutError as e:
    print("Your request time out!")
    


