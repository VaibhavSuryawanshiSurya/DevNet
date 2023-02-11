import requests

URL = "http://10.10.20.159/xmlapi/session/begin"

HEADERS = {
    'Authorization': "Basic ZGV2YXNjOkMxc2NvITIz"
 }

RESPONSE = requests.request("POST", URL,
headers=HEADERS)
print(RESPONSE.headers["Set-Cookie"])