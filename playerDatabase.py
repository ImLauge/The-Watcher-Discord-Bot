import sqlite3
import inspect
import os.path
import discord
import steamData

    # if the table isnt created then create it and need only be ran once

def create_player_table():
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename))
    print("DB Path :" + path)
    conn = sqlite3.connect(path + '/TheWatcher.db')
    c = conn.cursor()
    c.execute(
        'CREATE TABLE IF NOT EXISTS playerNameChange(playerID INTEGER, originalName TEXT, newName TEXT)')
    conn.commit()
    c.close()
    conn.close()

    # add dynamic data to the player table

def add_player_data(playerID, originalName, newName):
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename))
    conn = sqlite3.connect(path + '/TheWatcher.db')
    c = conn.cursor()
    c.execute("INSERT INTO playerNameChange (playerID, originalName, newName) VALUES (?, ?, ?)",
              (playerID, originalName, newName))
    conn.commit()
    c.close()
    conn.close()

    # update current player name

def update_player_name(playerID, newName):
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename))
    conn = sqlite3.connect(path + '/TheWatcher.db')
    c = conn.cursor()
    c.execute("UPDATE playerNameChange SET newName =? WHERE playerID = ?",
              (newName, playerID))
    conn.commit()
    c.close()
    conn.close()


def read_existing_player_data():
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename))
    conn = sqlite3.connect(path + '/TheWatcher.db')
    c = conn.cursor()
    players = []
    players = c.execute("SELECT * FROM  playerNameChange").fetchall()
    conn.commit()
    c.close()
    conn.close()
    return players


def check_for_existing_player(playerid):
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename))
    conn = sqlite3.connect(path + '/TheWatcher.db')
    c = conn.cursor()
    players = []
    players = c.execute(
        "SELECT playerID, originalName, newName  FROM  playerNameChange WHERE playerID =?", (playerid,)).fetchall()
    conn.commit()
    c.close()
    conn.close()
    return players


def lookup_player_id(playerid):
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename))
    conn = sqlite3.connect(path + '/TheWatcher.db')
    c = conn.cursor()
    lookup_query = "SELECT playerID, originalName, newName  FROM  playerNameChange WHERE playerID =?"
    player = c.execute(lookup_query, (playerid,)).fetchone()
    conn.commit()
    c.close()
    conn.close()
    return player

def lookup_player_embed(playerid, api_key):
    playerList = lookup_player_id(playerid)
    avatar = steamData.grabProfileData(playerid, api_key)
    embed = discord.Embed(title=str(playerList[1]),
                              url=f"https://steamcommunity.com/profiles/" +
                                  str(playerList[0]),
                              description='Current Name = ' + str(playerList[2]))
    embed.set_thumbnail(url=avatar)
    return embed

def get_DB_linked_player_Embed_List(playerid=None):
    newList = []
    if playerid is None:
        playerList = read_existing_player_data()
        for p in playerList:
            embed = discord.Embed(title=str(p[1]),
                              url=f"https://steamcommunity.com/profiles/" +
                                  str(p[0]),
                              description='Current Name = ' + str(p[2]))
            newList.append(embed)
    else:
        print("else")
        playerList = lookup_player_id(playerid)
        for p in playerList:
            embed = discord.Embed(title=str(p[1]),
                              url=f"https://steamcommunity.com/profiles/" +
                                  str(p[0]),
                              description='Current Name = ' + str(p[2]))
            newList.append(embed)
            print(playerList)
        print("after for loop")
    return newList
