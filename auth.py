import json
import random
import requests
import os.path
from os import path

from yggdrasil import authenticate
from requests_toolbelt.utils import dump

import os.path
askInput = True
from os import path
if path.exists("auth.json"):
    with open('auth.json', 'r') as data:
        config = json.load(data)
        if config["useConfigCredentials"]:
            # Lets use saved data
            askInput = False
            username = config["username"]
            password = config["password"]
            print("Using credentials from file automatically")


print("Welcome to the Beta Evolutions Authenticator")

if askInput:
    print("\n\nPlease enter your Mojang Username:")
    username = input()
    print("Please enter your Mojang Password:")
    password = input()
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAttempting authentication")

randomClientToken = random.randint(10000, 99999)
try:
    mc = authenticate(username, password, 'Minecraft', randomClientToken, False)
    # Stage 1
    playerName = mc['selectedProfile']['name']
    playerID = mc['selectedProfile']['id']
    playerToken = mc['accessToken']
    try:
        content = requests.get("https://auth.johnymuffin.com/userAuth.php?method=1&username=" + playerName)
        stage1 = json.loads(content.content)
        serverID = stage1['serverId']

        content = requests.get("http://session.minecraft.net/game/joinserver.jsp?user=" + playerName + "&sessionId=token:" + playerToken + ":" + playerID + "&serverId=" + serverID)
        content = content.text
        if content != "OK":
            print("Mojang rejected the credentials")
        else:
            content = requests.get("https://auth.johnymuffin.com/userAuth.php?method=2&username=" + playerName + "&serverId=" + serverID)
            stage3 = json.loads(content.content)
            if stage3["result"] == True:
                print("You have been Authenticated Sucessfully")
            else:
                print("Authentication Failed :(")

    # Stage 3
    except:
        print("Sorry, We are having an error with our API")

    # Stage 2
except:
    print("Sorry, The Credentials Entered Are Incorrect")

if(askInput):
    print("Press the Enter to close")
    x = input()
else:
    print("Complete, Shutting Down")
