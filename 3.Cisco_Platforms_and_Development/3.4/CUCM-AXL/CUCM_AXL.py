from ciscoaxl import axl
CUCM = '10.10.20.1'
CUCM_USER = "administrator"
CUCM_PASSWORD = "ciscopsdt"
CUCM_VERSION = '14.0'

ucm = axl(username=CUCM_USER,password=CUCM_PASSWORD,cucm=CUCM,cucm_version=CUCM_VERSION)
print (ucm)

for phone in ucm.get_phones():
    print(phone.name)
for user in ucm.get_users():
    print(user.firstName)