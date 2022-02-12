import weapons

def play():
    print("Welcome to Dungeon Trek!")
    inventory = [weapons.Dagger(), "gold", "bread"]
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
            print("Inventory:")
            for item in inventory:
                print('* ' + (str(item)))
        elif action_input in ['li', 'long inventory']:
            print("Inventory:")
            for item in inventory:
                if hasattr(item, "description"):
                    print('* ' + (str(item)) + ": " + item.description)
                else:
                    print('* ' + (str(item)))
        else:
            print("Invalid action!")

def get_player_command():
    return input(">>> ")

play()
