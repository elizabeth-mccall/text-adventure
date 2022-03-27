from vocab import *
from parser import *

#################
### GAME LOOP ###
#################

def play():
    print('''
Welcome to Dungeon Trek!
(c) Elizabeth McCall

Enter "help" for a list of commands. Enter "quit" to quit the game.
''')
    print(get_room(player.x, player.y))
    get_room(player.x, player.y).describe()
    print("")
    while True:
        get_room(player.x, player.y).update()
        command = input(">").lower().split()
        if check(command) == True:
            parse(command)
        # print("For debugging: Your coordinates are ({}, {})".format(player.x, player.y))
        print("")

play()