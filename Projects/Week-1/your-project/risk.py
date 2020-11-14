#!/usr/bin/env python3
#make the file exectuable 

#put stuff in functions

# --------------------------------------
# INITIALIZE 

#import colors for background
#from colorama import Fore

class Player:
    def __init__(self, name, soldiers):
        self.name = name
        self.soldiers = soldiers
        
def play_game():
    phase_initialize()

def phase_initialize():

    #get list of players (limit: six players)
    players_lst = ["delete me"]
    while players_lst[-1] != "q":
        players_lst.append(input("Please insert a player's name or ‘q’ once finished\n"))
        if len(players_lst) > 7:
            print("""This game is limited to 6 participents.\n
                Let's start over.""")
            players_lst = ["delete me"]
    players_lst = players_lst[1:-1]


    #print(players_lst)

    #create object names
    players_enu = [""]
    for i, x in enumerate(range(len(players_lst))):
        players_enu.append("player_"+str(i))
    players_enu = players_enu[1:]
    #print(players_enu)


    # create objects from list of object names
    for i, x in enumerate(players_enu):
       # print(x)
        globals()[x] = Player(players_lst[i], init_soldiers(len(players_lst)))
       # print(globals()[x].name)

    #print(player_1.name)
    #print(player_1.soldiers)



# --------------------------------------
# BOARD SETUP

def init_soldiers(num_players):
    """
    If 2 are playing, see special instructions.If 3 are playing, each player counts out 35 Infantry.If 4 are playing, 
    each player counts out 30 Infantry.
    If 5 are playing, each player counts out 25 Infantry.If 6 are playing, each player counts out 20 Infantry.
    """
    if num_players == 2:
        return(40) # notice - it's not following the O.G rules. 
    elif num_players == 3:
        return(35)
    elif num_players == 4:
        return(30)
    elif num_players == 5:
        return(25)
    elif num_players == 6:
        print(20)
        
# --------------------------------------
# RUN GAME

play_game()

print(player_1.soldiers)
