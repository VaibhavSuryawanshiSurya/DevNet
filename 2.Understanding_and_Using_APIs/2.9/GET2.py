import requests
from pprint import pprint 


url = "https://postman-echo.com/basic-auth"

payload={}
headers = {
  'Authorization': 'Basic cG9zdG1hbjpwYXNzd29yZA==',
  'Cookie': 'sails.sid=s%3AhYE505vl3M2U9rnGp-923XQAZ7VnhiQE.Pu7r%2FhVo9yd4M4yEYEh3g0YQXk3WsGKlCmshP%2Bhz8aU'
}

response = requests.request("GET", url, headers=headers, data=payload).json()

pprint(response)
