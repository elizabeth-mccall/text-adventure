from player import Player

def play():
    print("Welcome to Dungeon Trek!")
    player = Player()
    while True:
        action_input = get_player_command()
        if action_input in ['n', 'N', 'north']:
            print("Go North!")
        elif action_input in ['s', 'S', 'south']:
            print("Go South!")
        elif action_input in ['e', 'E', 'east']:
            print("Go East!")
        elif action_input in ['w', 'W', 'west']:
            print("Go West!")
        elif action_input in ['i', 'I', 'inventory']:
            player.print_inventory()
        else:
            print("Invalid action!")


def get_player_command():
    return input("Action: ")

play()
