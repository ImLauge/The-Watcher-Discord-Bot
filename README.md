# The-Watcher-Discord-Bot For the game Rust

Fork notes:
I stumbled upon this bot, and it was exactly what I was looking for. Going into this I had no previous coding experience, so going head first into this was quite a challenge. I couldn't make the name change notifications work, which was the main thing I wanted, so that was the first step. After, with the help of a colleague, fixing that. I started adding features to the best of my abilities, some of those features were:

- Announcements when a new player has been added
- Profile pictures to embed player lookup
- Manually adding players to database
- Reworking the command system and adding new commands

Original readme:

A Discord Watcher bot for the game Rust.
Yes i play the game Rust by Facepunch and i want to keep track of players who login and log out and how long they played for, so i created a discord bot to do this for me.

I have this Bot running on a Raspberry pi4 with DietPi Operating system so it runs 24/7.

It tracks players joined/logged and play time in Rust game servers via Battlemetrics.com so you need to find the server you want to track in battlemetrics and paste in the url to the setup config file.

You can track when a player changes their name but the server needs to be connected to playrust.io and the bot will automatically create an sqllite3 database and start storing player names and name changes, although this isnt fully tested and could be improved.

When the Discord bot is up and running you can use the command 
(>help) command to display possible commands such as 
(>players) :gets all the current players
(>pinfo) :get all players from the database (still needs work to get by name etc)

Note: this can work for other games too but i only care about Rust ;-)

## Prerequisites for this project to work:

You need python 3.7 or higher to run this project.

py -3 -m pip install -U discord.py

py -3 -m pip install -U requests

py -3 -m pip install -U beautifulsoup4

## To start a terminal in DietPi
make a file called launchMe.sh or what ever you want to call it and add the following
```
xterm -e python3.7 /root/Desktop/The-Watcher-Discord-Bot/main.py
```

## To have the Discord Bot launch on login to the DietPi Desktop

1. /root
2. right click and show hidden files
3. go in to the .config folder
4. then in the autostart folder
5. make a file (myfile.desktop)
6. in the file put the following

```
[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=<GUI Controller>
Comment=
Exec= python3.7 /root/Desktop/The-Watcher-Discord-Bot/main.py
StartupNotify=false
Terminal=true
Hidden=false
```

The above code will launch the python files in a visible terminal window.
Obviously i put my files on the desktop so you should do the same or choose your own location.

## In the Setup Folder enter in your setup, there is an explaination on how to set it up too.

I will update with pictures later on so that you can see what the bot does.

Philip M



