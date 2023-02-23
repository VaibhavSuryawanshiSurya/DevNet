from webexteamssdk import WebexTeamsAPI


api = WebexTeamsAPI(access_token='ZDQ5NTFiNDktMDA0Ny00Yzg4LTkyYWYtNTBmZjA5MThmMzlmNmJkZTc2NGItM2Fj_P0A1_1042ee4d-8548-4fc3-baae-4c6f003181a7')


#### GET TEAM INFO ###
teams = api.teams.list()

for team in teams:
    print(team)
    if getattr(team, 'name') != 'DevNet Team':
        create_team = api.teams.create('DevNet Team')
        teamId = getattr(create_team, 'id')
    else:
        teamId = team.id


###### PEOPLE #####
print(api.people.me())
print(api.people.list())
# api.people.create(emails=['ben.finkel@cbtnuggets.com'], displayName='Ben Finkel', firstName='Ben',
#                   lastName='Finkel', roles=['Y2lzY29zcGFyazovL3VzL1JPTEUvaWRfZnVsbF9hZG1pbg'])

#### ROLES #####
# roles = api.roles.list()
# # print(roles)
# for role in roles:
#     print(role)


#### ROOMS #####
rooms = api.rooms.list()
evaluator = False
for room in rooms:
    if room.title == 'DevNet Room':
        evaluator = True
        roomId = room.id

if evaluator == False:
    new_room = api.rooms.create('DevNet Room', teamId=teamId)
    roomId = new_room.id


#### MESSAGES ####
api.messages.create(roomId, text='Posted from the SDK')

# CLEANUP
# for room in rooms:
#     if getattr(room, 'title') == 'DevNet Room':
#         api.rooms.delete(getattr(room, 'id'))

# for team in teams:
#     if getattr(team, 'name') == 'DevNet Team':
#         api.teams.delete(getattr(team, 'id'))