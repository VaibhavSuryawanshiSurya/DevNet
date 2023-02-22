import os

from dotenv import load_dotenv

# Use given commands in Linux terminal to set environment variable
    # $ echo $HOME
    # $ export <variable_name> = "Value" ---> export SWITCHUSER='cisco'
    # $ echo $SWITCHUSER

user = os.environ.get("SWITCHUSER")
print(user)

# By using python-dotenv library
    # pip install python-dotenv
    # create .env file 

user = os.environ.get("CISCOUSER")
print(user)