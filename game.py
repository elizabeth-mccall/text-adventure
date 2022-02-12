class Weapon:
    def __str__(self):
        return self.name

class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust." 
        self.damage = 10

class RustySword(Weapon):
    def __init__(self):
        self.name = "Sword"
        self.description = "This sword is showing its age, but it still has some fight in it."
        self.damage = 20

class Crossbow(Weapon):
    def __init__(self):
        self.name = "Crossbow"
        self.description = "This crossbow can shoot quite a distance."
        self.damage = 20

def play():
    print("Welcome to Dungeon Trek!")
    inventory = [Dagger(), "Gold", "bread"]
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
                print('* ' + (str(item)))
        else:
            print("Invalid action!")


def get_player_command():
    return input("Action: ")

play()
