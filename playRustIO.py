from urllib import response
import requests
import json
import playerDatabase
import watcherLogging

def check_for_player_name_changes(server_ip, server_port):
    playerDbList = []
    myReturnList = []
    addedPlayersList = []
    try:
        resp = requests.get("http://" + server_ip + ":" +
                            server_port + "/recent.json")

        # print(resp.content)
        print("Checking recent players on " + server_ip + ":" + server_port)

        players = json.loads(resp.content) 
        for p in players:
            playerDbList = playerDatabase.check_for_existing_player(
                p['id'])
            if len(playerDbList) > 0:
                for pData in playerDbList:
                    if pData[2] != p['name']:
                        # check if the name has changed
                        playerDatabase.update_player_name(p['id'], p['name'])
                        myReturnList.append(
                            "Player ::" + pData[1] + " Now Playing as ::" + p['name'] + '\n')
                        #print("player changed name")
                        print("Player ::" + pData[1] + " Now Playing as ::" + p['name'] + '\n')
            else:
                 # add new player to the database
                playerDatabase.add_player_data(
                    p['id'], p['name'], p['name'])
                addedPlayersList.append("Added new player :: Id: " + p['id'] + " Name: " + p['name'] + "\n")

            # add or check player in the database

    except Exception as e:
        print("Error has occured in PlayRust.io request check_for_player_name_changes ::" + str(e))
        watcherLogging.error_logs(
            'Error has occured in PlayRust.io request check_for_player_name_changes ::' + str(e))

    return myReturnList, addedPlayersList