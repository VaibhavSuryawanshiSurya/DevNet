import requests

url = "https://swapi.dev/api/people/2/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
