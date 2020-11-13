#!/usr/bin/env python3
#make the file exectuable 

# --------------------------------------
# INITIALIZE 

#import colors for background
#from colorama import Fore

class Player:
    def __init__(self, name):
        self.name = name

#get list of players
players_lst = ["delete me"]
while players_lst[-1] != "q":
    players_lst.append(input("Please insert a player's name or ‘q’ once finished\n"))
players_lst = players_lst[1:-1]


print(players_lst)

#create object names
players_enu = [""]
for i, x in enumerate(range(len(players_lst))):
    players_enu.append("player_"+str(i))
players_enu = players_enu[1:]
print(players_enu)

#fix a max 

# create objects from list of object names
for i, x in enumerate(players_enu):
    print(x)
    x = Player(players_lst[i])
    print(x.name)

print(player_1.name)


# --------------------------------------
# BOARD SETUP
