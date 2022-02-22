from player import Player
import world

def play():
    print("Welcome to Dungeon Trek!")
    player = Player()
    while True:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        action_input = get_player_command()
        if action_input in ['n', 'N', 'north']:
            player.move_north()
        elif action_input in ['s', 'S', 'south']:
            player.move_south()
        elif action_input in ['e', 'E', 'east']:
            player.move_east()
        elif action_input in ['w', 'W', 'west']:
            player.move_west()
        elif action_input in ['i', 'I', 'inventory']:
            player.print_inventory()
        else:
            print("Invalid action!")


def get_player_command():
    return input("Action: ")

play()
