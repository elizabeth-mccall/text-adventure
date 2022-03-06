###############
## COMMANDS ###
###############

#MOVEMENT
from importlib.resources import contents


verb_move = ["go", "walk", "move", "head"]
directions = ["north", "south", "east", "west", "up", "down"]
directions_short = ["n", "e", "w", "s", "u", "d"]

#INVENTORY
verb_inventory = ["i", "inventory"]

#LOOK
verb_look = ["l", "look"]

#ATTACK
verb_attack = ["attack", "hit", "strike", "kill"]

#EXAMINE
verb_examine = ["x", "examine", "inspect", "investigate", "study", "look at"]

#TAKE/DROP
verb_take = ["take"]
verb_drop = ["drop"]

#EAT/DRINK
verb_eat = ["eat", "bite"]
verb_drink = ["drink"]

#GAME COMMANDS
cmd_help = ["h", "help"]
cmd_quit = ["q", "quit"]

#PREP
prep_from = ["from", "out"]
prep_of = ["of"]

#OTHER
word_all = ["all", "everything"]

###############
### OBJECTS ###
###############

class Thing:
    def __init__(self, name, description, **kwargs):
        self.name = name
        self.description = description
    def __str__(self):
        return self.name
    def describe(self):
        print(self.description) 

class Container(Thing):
    def __init__(self, name, description, contents, **kwargs):
        self.contents = contents
        super().__init__(name, description, **kwargs)
    def get_contents(self):
        return self.contents
    def whats_inside(self):
        inside = ""
        if self.contents != []:
            for item in self.contents:
                inside += "* a "
                inside += str(item)
                if item != self.contents[-1]:
                    inside += "\n"
            return inside
        elif self.contents == []:
            return "nothing"
    def describe(self):
        if self.contents != []:
            print(str(self.description), "containing:")
            print(self.whats_inside())
        else:
            print((self.description) + " with " + str(self.whats_inside()) + " inside.")
    def take_out(self, item, location):
        if self.contents != []:
            self.contents.remove(item)
            location.append(item)
        else:
            raise ValueError

class Food(Thing):
    def __init__(self, name, description, **kwargs):
        super().__init__(name, description, **kwargs)

bread = Food(name = "slice of bread", description = "A slightly stale slice of wheat bread.", edible = True)
sword = Thing(name="glowing sword", description="A glowing sword.")
branch = Thing(name="branch", description="A tree branch.")
jar = Container(name = "jar", description="An empty jar", contents = [])
bottle = Container(name = "bottle", description="A small glass bottle", contents = ["bit of water"])
basket = Container(name= "basket", description="A woven basket", contents = [jar, bottle, "knife"])

class Room():
    def __init__(self, x, y, contents = [], description = ""):
        self.x = x
        self.y = y
        self.contents = contents
        self.description = description
    def describe(self):
        print(self.description)
        inside = "You see a "
        if self.contents != []:
            for item in self.contents:
                if item == self.contents[0]:
                    inside += (str(item))
                elif item == self.contents[-1]:
                    inside += (", and a " + str(item))
                else:
                    inside += (", " + str(item))
            inside += " in here."
            print(inside)  
    def take(self, item, location):
        if item in self.contents:
            self.contents.remove(item)
            location.append(item)
        else:
            raise ValueError     
    def take_all(self, location):
        if self.contents != []:
            return_list = []
            for item in self.contents:
                location.append(item)
                return_list.append(item)
            self.contents.clear()
            return return_list
        else:
            raise ValueError

class RegularRoom(Room):
    def __init__(self, x, y, contents = [basket, jar, bottle], description = "It's just a room."):
        self.x = x
        self.y = y
        self.contents = contents
        self.description = description
    def __str__(self):
        return "Regular Room"

class CoolRoom(Room):
    def __init__(self, x, y, contents = [sword, bread], description = "This is a pretty cool room."):
        self.x = x
        self.y = y
        self.contents = contents
        self.description = description
    def __str__(self):
        return "Cool Room"

class StartRoom(Room):
    def __init__(self, x, y, contents = [branch], description = "This is the starting room."):
        self.x = x
        self.y = y
        self.contents = contents
        self.description = description
    def __str__(self):
        return "Starting Room"

class EmptyRoom(Room):
    def __init__(self, x, y, contents = [], description = "Just an empty room."):
        self.x = x
        self.y = y
        self.contents = contents
        self.description = description
    def __str__(self):
        return "Empty Room"

world = [
    [CoolRoom(0,0), CoolRoom(1,0), RegularRoom(2,0)],
    [CoolRoom(0,1), RegularRoom(1,1), StartRoom(2,1)],
    [RegularRoom(0,2), EmptyRoom(1,2), RegularRoom(2,2)]
]

start_location = 2, 1

def get_room(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world[y][x]
    except IndexError:
        return None

class Player():
    def __init__(self):
        self.description = "It's just you."
        self.contents = []
        self.x = start_location[0]
        self.y = start_location[1]
    def describe(self):
        print(self.description)
    def whats_inside(self):
        inside = ""
        if self.contents != []:
            for item in self.contents:
                if isinstance(item, Container):
                    inside += "* a "
                    inside += str(item)
                    inside += (" which contains:")
                    inside += "\n"
                    if item.whats_inside() == "nothing":
                        inside += '''   nothing'''
                        if item == self.contents[-1]:
                            continue
                        inside += "\n"
                    else:
                        for content in item.get_contents():
                            inside += '''   * a '''
                            inside += str(content)
                            if content != item.get_contents()[-1]:
                                inside += "\n"
                        if item != self.contents[-1]:
                            inside += "\n"
                else:
                    inside += "* a "
                    inside += str(item)
                    if item != self.contents[-1]:
                        inside += "\n"
            print(inside)
        elif self.contents == []:
            print("nothing")
    def inventory(self):
        print("You are carrying:")
        self.whats_inside()
    def move(self, dx, dy):
        old_x = self.x
        old_y = self.y
        self.x += dx
        self.y += dy
        new_room = get_room(self.x, self.y)
        if new_room == None:
            self.x = old_x
            self.y = old_y
            print("You can't go that way.")
        else:
            print(new_room)
            new_room.describe()
    def move_direction(self, direction):
        if direction == "north":
            self.move(dx = 0, dy = -1)
        elif direction == "south":
            self.move(dx = 0, dy = 1)
        elif direction == "east":
            self.move(dx = 1, dy = 0)
        elif direction == "west":
            self.move(dx = -1, dy = 0)
        else:
            print("I don't recognize that direction.")
    def drop(self, item, location):
        if item in self.contents:
            self.contents.remove(item)
            location.append(item)
        else:
            raise ValueError
    def drop_all(self, location):
        if self.contents != []:
            return_list = []
            for item in self.contents:
                location.append(item)
                return_list.append(item)
            self.contents.clear()
            return return_list
        else:
            raise ValueError
    def eat(self, item):
        if item in self.contents:
            if isinstance(item, Food):
                self.contents.remove(item)
            else:
                raise AttributeError
        else:
            raise ValueError

player = Player()

item_dict = {
    "sword": sword,
    "branch": branch,
    "basket": basket,
    "jar": jar,
    "bottle": bottle,
    "bread": bread,
    "self": player}

#ALL
all_commands = [verb_move, directions, directions_short, verb_inventory, verb_look, verb_attack, verb_examine, cmd_quit, cmd_help, verb_take, verb_drop, verb_eat, verb_drink, prep_from, prep_of, item_dict, word_all]

#Checks whether all words are in vocabulary
def check(command):
    if len(command) == 0:
        print("I beg your pardon?")
        return False
    else:
        for command_word in command:
            checker = False
            for word_list in all_commands:
                if command_word in word_list:
                    # for debugging: print("I understand", command_word)
                    checker = True
                else:
                    pass
            if checker == False:
                print('''I don't know the word "''' + str(command_word) + '".')
                return False
        if checker == True:
            return True

def parse(command):
    #MOVEMENT
    if any(word in directions for word in command) or any(word in directions_short for word in command) or any(word in verb_move for word in command):
        if command[0] in directions:
            if len(command) == 1:
                player.move_direction(command[0])
            else:
                print("I understand you as far as wanting to move", str(command[0]) + ".")
        elif command[0] in directions_short:
            command_direction = None
            for direction in directions:
                if command[0] == direction[0]:
                    command_direction = direction
                else:
                    pass
            print("Shortcut -- Execute the move function with", command_direction, "as a direction.")
        elif command[0] in verb_move:
            if len(command) == 1:
                print("Where do you want to", str(command[0]) + "?")
            elif len(command) == 2:
                if command[1] in directions or command[1] in directions_short:
                    print("Execute move function with", command[1], "as a direction.")
                else:
                    print('"' + str(command[1].capitalize()) + '" is not a direction.')
            else:
                print("I don't understand where you want to", command[0])
        else:
            def is_movement(word):
                return word in directions or word in directions_short or word in verb_move
            desired_direction = [word for index, word in enumerate(command) if is_movement(word)]
            print('''I don't understand how you used the word "''' + str(desired_direction[0]) + '".')
    #INVENTORY
    elif command[0] in verb_inventory:
        if len(command) == 1: 
            player.inventory()
        else:
            print("I understood you as far as wanting to take inventory.")
    #LOOK
    elif command[0] in verb_look:
        if len(command) == 1:
            print(get_room(player.x, player.y))
            get_room(player.x, player.y).describe()
        else:
            print("I understood you as far as wanting to look.")
    #EXAMINE
    elif command[0] in verb_examine:
        if len(command) == 1:
            print("What do you want to", str(command[0]) + "?")
        else: 
            try:
                if command[1] in word_all:
                    print("It's not clear what you're referring to.")
                elif command[1] == "self" or item_dict[command[1]] in get_room(player.x, player.y).contents or item_dict[command[1]] in player.contents:
                    item_dict[command[1]].describe()
                else:
                    print("You can't see a {} here!".format(command[1]))
            except KeyError:
                print("I understood you as far as wanting to examine something.")
    #TAKE
    elif command[0] in verb_take:
        def take_out_of(item, container):
            try:
                item_dict[container].take_out(item_dict[item], player.contents)
                print("You take the {} from the {}.".format(item, container))
            except ValueError:
                print("There is no {} in the {}.".format(item, container))
            except AttributeError:
                print("The {} is not a container.".format(container))
            except KeyError:
                print("I understood you as far as wanting to take something.")
        def take(item):
            try:
                get_room(player.x, player.y).take(item_dict[item], player.contents)
                print("Taken.")
            except ValueError:
                print("That's not in here!")
            except KeyError:
                print("I understood you as far as wanting to take something.")
        def take_all():
            try:
                for item in get_room(player.x, player.y).take_all(player.contents):
                    print("Taken: {}".format(item))
            except ValueError:
                print("There's nothing here to take.")
            except KeyError:
                print("I understood you as far as wanting to take something.")
        if len(command) == 1:
            print("What do you want to", str(command[0]) + "?")
        elif len(command) == 2:
            if command[1] in word_all:
                take_all()
            else:
                take(command[1])
        elif len(command) == 3:
            take_out_of(command[1], command[2])
        elif len(command) == 4:
            if command[2] in prep_from:
              take_out_of(command[1], command[3])
            else:
                pass
        elif len(command) == 5:
            if command[2] in prep_from and command[3] in prep_of:
                take_out_of(command[1], command[4])
            else:
                pass
        else:
            print("I understood as far as you wanting to take something.")
    #DROP
    elif command[0] in verb_drop:
        def drop(item):
            try:
                player.drop(item_dict[item], get_room(player.x, player.y).contents)
                print("Dropped.")
            except ValueError:
                print("You don't have that.")
        def drop_all():
            try:
                for item in player.drop_all(get_room(player.x, player.y).contents):
                    print("Dropped: {}".format(item))
            except ValueError:
                print("You aren't carrying anything.")
        if len(command) == 1:
            print("What do you want to", str(command[0] + "?"))
        elif len(command) == 2:
            if command[1] in word_all:
                drop_all()
            else:
                drop(command[1])
        else:
            print("I understood as far as you wanting to drop something.")
    #EAT
    elif command[0] in verb_eat:
        def eat(item):
            try:
                player.eat(item_dict[item])
                print("You eat the {}. Yum!".format(item_dict[item]))
            except AttributeError:
                print("You can't eat that!!")
            except ValueError:
                print("You don't have that.")
            except KeyError:
                print("I don't understand what you want to eat.")
        if len(command) == 1:
            print("What do you want to eat?)")
        elif len(command) == 2:
            eat(command[1])
    #HELP
    elif command[0] in cmd_help:
        if len(command) == 1:
            print("Help menu.")
        else:
            print("Type 'help' if you need help.")
    #QUIT
    elif command[0] in cmd_quit:
        if len(command) == 1:
            quit_y_n = input("Are you sure you want to quit? Y/N \n \n>")
            if quit_y_n == "y":
                print("Quitting game.")
                raise SystemExit
            else:
                print("Okay, then.")
        else:
            print("Type 'quit' if you want to quit.")
    else:
        print("Sorry, but you stumped me with that one.")

def play():
    while True:
        command = input(">").lower().split()
        if check(command) == True:
            parse(command)
        print("For debugging: Your coordinates are ({}, {})".format(player.x, player.y))
        print("")

play()


