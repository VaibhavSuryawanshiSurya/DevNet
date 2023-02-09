import json

jsonstr = """ {
    "people":
    [
        {
            "Id":"1",
            "FirstName":"VAibhav",
            "LastName" :"Suryawanshi",
            "Email"    :"vaibhav.suryawanshi@gmail.com"
        },
        {
            "Id":"2",
            "FirstName":"Vishal",
            "LastName" :"Deshmukh",
            "Email"    :"vishal.deshmukh@gmail.com"
        },
        {
            "Id":"3",
            "FirstName":"Aniket",
            "LastName" :"Shigade",
            "Email"    :"aniket.shigade@gmail.com"
        }

    ]
} """

# loads function take must be str, bytes or bytearray 
jsonobj = json.loads(jsonstr)
print(type(jsonobj))
print(jsonobj)


# load function take wrapper object
jsonobj = json.load(open('sample.json','r'))
print(jsonobj)