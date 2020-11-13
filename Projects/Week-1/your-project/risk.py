#!/usr/bin/env python3
#make the file exectuable 

#put stuff in functions

# --------------------------------------
# INITIALIZE 

#import colors for background
#from colorama import Fore

class Player:
    def __init__(self, name):
        self.name = name

#get list of players (limit: six players)
players_lst = ["delete me"]
while players_lst[-1] != "q":
    players_lst.append(input("Please insert a player's name or ‘q’ once finished\n"))
    if len(players_lst) > 7:
        print("""This game is limited to 6 participents.\n
              Let's start over.""")
        players_lst = ["delete me"]
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
    globals()[x] = Player(players_lst[i])
    #print(globals()[x].name)

print(player_1.name)


# --------------------------------------
# BOARD SETUP

"""
If 2 are playing, see special instructions.If 3 are playing, each player counts out 35 Infantry.If 4 are playing, 
each player counts out 30 Infantry.
If 5 are playing, each player counts out 25 Infantry.If 6 are playing, each player counts out 20 Infantry.
"""
if len(players_lst) == 2:
    print("2")
elif len(players_lst) == 3:
    print("3")
elif len(players_lst) == 4:
    print("4")
elif len(players_lst) == 5:
    print("5")
elif len(players_lst) == 6:
    print("6")
