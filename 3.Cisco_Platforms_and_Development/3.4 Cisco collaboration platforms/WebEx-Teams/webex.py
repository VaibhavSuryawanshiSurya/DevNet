import requests
import json

# Get your token here after logging in: https://developer.webex.com/docs/api/getting-started
token = 'ZDQ5NTFiNDktMDA0Ny00Yzg4LTkyYWYtNTBmZjA5MThmMzlmNmJkZTc2NGItM2Fj_P0A1_1042ee4d-8548-4fc3-baae-4c6f003181a7'

### Create a Team ###
teams_url = 'https://api.ciscospark.com/v1/teams'
headers = {'Authorization': f'Bearer {token}',
           'Content-Type': 'application/json'}

teams_body = {
    "name": "DevNet Team"
}

post_response = requests.post(
    teams_url, headers=headers, data=json.dumps(teams_body), verify=False).json()
print(post_response)


get_response = requests.get(teams_url, headers=headers,verify=False).json()
#teamId = get_response['items'][0]['id']
teams = get_response['items']
for team in teams:
    if team['name'] == 'DevNet Team':
        teamId = team['id']


###### CREATE A ROOM ########
room_url = 'https://api.ciscospark.com/v1/rooms'
room_body = {
    "title": "DevNet Room",
    "teamId": teamId
}


# room_post = requests.post(room_url, headers=headers,
#                           data=json.dumps(room_body)).json()
# print(room_post)


get_rooms = requests.get(room_url, headers=headers).json()
rooms = get_rooms['items']
for room in rooms:
    if room['title'] == 'DevNet Room':
        roomId = room['id']


#### POST A MESSAGE TO THE ROOM ####
msg_url = 'https://api.ciscospark.com/v1/messages'
msg_body = {
    "roomId": roomId,
    'text': 'ALERT: Interface on device XYZ is down'
}

msg_response = requests.post(
    msg_url, headers=headers, data=json.dumps(msg_body)).json()