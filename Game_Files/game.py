import world
from player import Player

def play():
    print('''
Welcome to Dungeon Trek!
    
(c) Elizabeth McCall
written in Python
    
Enter "q" to quit. Enter "h" for help.
    
    ''')
    world.parse_world_dsl()
    player = Player()
    room = world.tile_at(player.x, player.y)
    print(room)
    print(room.description())
    room.mark_visited()
    while True:
        room = world.tile_at(player.x, player.y)
        print("For debugging: Your current location is {} (coordinates {}, {}).".format(room, player.x, player.y))
        player_input = (input(">>>")).lower()
        if player_input in ["n", "s", "e", "w", "north", "south", "east", "west"]:
            if player_input in ["n", "north"]:
                player.move_north()
            elif player_input in ["s", "south"]:
                player.move_south()
            elif player_input in ["w", "west"]:
                player.move_west()
            elif player_input in ["e", "east"]:
                player.move_east()
        elif player_input in ["l", "look"]:
            print(world.tile_at(player.x, player.y).description())
        elif player_input in ["q", "quit"]:
            return
        elif player_input in ["h", "help"]:
            print('''
Commands: 

n , north = move north
s , south = move south
e , east = move east
w , west = move west
h , help = help
l , look = look around the room
i , inventory = check inventory
q, quit = exit game
''')
        else:
            print("I don't know that command.")


play()