import requests
from pprint import pprint 

url = "https://swapi.dev/api/people/2/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload).json()

print(response)
