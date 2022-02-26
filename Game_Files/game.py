import world
from player import Player

def play():
    print("Welcome to Dungeon Trek!")
    world.parse_world_dsl()
    player = Player()
    room = world.tile_at(player.x, player.y)
    print(room)
    print(room.description())
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
                print(new_room.description())
        elif player_input in ["l", "look"]:
            print(room.description())
        elif player_input in ["q", "quit"]:
            return
        else:
            print("I don't know that command.")


play()