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
        old_x = player.x
        old_y = player.y
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
            new_room = world.tile_at(player.x, player.y)
            if new_room == None:
                print("You can't go that way.")
                player.x = old_x
                player.y = old_y
            else:
                print(new_room)
                if new_room.visited == False:
                    print(new_room.description())
                    new_room.mark_visited()
                else:
                    pass
        elif player_input in ["l", "look"]:
            print(room.description())
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