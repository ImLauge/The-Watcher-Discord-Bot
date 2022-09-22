from urllib import response
import requests
import json

def grabProfileData(steamID, key):
    resp = requests.get(
        "https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key="
        + key + "&steamids=" + steamID)
    if resp.status_code == 200:
        print("requesting")
        data = resp.json()
        avatar = data["response"]["players"][0]["avatarfull"]
    else:
        print("Got no response from Steam")
    return avatar