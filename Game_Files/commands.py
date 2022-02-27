# def take_inventory():
#     print("Take inventory")

# def go_north():
#     return "go north"

# def go_south():
#     return "go south"

# def go_west():
#     return "go west"

# def go_east():
#     return "go east"

# def take_item():
#     return "take item"

# def help_menu():
#     return "Help menu"

# def look():
#     return "Look."

# commands = {
#     ("i", "inventory"): take_inventory,
#     ("n", "north"): go_north,
#     ("s", "south"): go_south,
#     ("e", "east"): go_east,
#     ("w", "west"): go_west,
#     ("t", "take", "grab", "pick"): take_item,
#     ("h", "help"): help_menu,
#     ("l", "look"): look}

# player_input = input(">").lower()

# for command_tuple in commands:
#     if player_input in command_tuple:
#         func = commands.get(command_tuple)
#     else:
#         pass

# print(func)

# print(commands.keys())
# print(commands.values())

class Guy:
    def __init__(self):
        self.x = 1
        self.y = 1
        self.inventory = ["bread", "cheese"]
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def move_north(self):
        self.move(dx = 0, dy = -1)
    def move_south(self):
        self.move(dx = 0, dy = 1)
    def print_inventory(self):
        for i in self.inventory:
            print("*", i)

Fred = Guy()

example = {
    ("n", "north"): Fred.move_north,
    ("s", "south"): Fred.move_south,
    ("i", "inventory"): Fred.print_inventory
}

def find_command(choice):
    for command_tuple in example:
        if choice in command_tuple:
            func = example.get(command_tuple)
            func()
        else:
            pass

while True:
    player_input = str(input(">").lower())
    find_command(player_input)
    print(Fred.x, Fred.y)

