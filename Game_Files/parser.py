###############
## COMMANDS ###
###############

#MOVEMENT
from tkinter import W


verb_move = ["go", "walk", "move", "head"]
directions = ["north", "south", "east", "west"]
directions_short = ["n", "e", "w", "s"]

#INVENTORY
verb_inventory = ["i", "inventory"]

#LOOK
verb_look = ["l", "look"]

#BREAK
verb_break = ["break", "smash", "shatter"]

#EXAMINE
verb_examine = ["x", "examine", "inspect", "investigate", "study", "look at"]

#TAKE/DROP
verb_take = ["take"]
verb_drop = ["drop"]

#EAT/DRINK
verb_eat = ["eat", "bite"]

#PUSH
verb_push = ["push", "pull", "budge", "shove"]

#SELF
word_self = ["myself", "me", "self"]

#GAME COMMANDS
cmd_help = ["h", "help"]
cmd_quit = ["q", "quit"]

#PREP
prep_from = ["from", "out"]
prep_of = ["of"]

#ARTICLES
articles = ["a", "an", "the"]

#OTHER
word_all = ["all", "everything"]

###############
### OBJECTS ###
###############

class Thing:
    def __init__(self, name, description, **kwargs):
        self.name = name
        self.description = description
        self.__dict__.update(kwargs)
    def __str__(self):
        return self.name
    def describe(self):
        print(self.description) 
    def breakit(self, location):
        if self.breakable == True:
            self.name = "broken " + self.name
            setattr(self, "broken", True)
            if isinstance(self, Container):
                for item in self.contents:
                    location.append(item)
                self.description += ", now broken and unable to hold anything."
                self.__class__ = Thing
            else:
                self.description += "Sadly, it is now broken."

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
                inside += f"* a {item}"
                if item != self.contents[-1]:
                    inside += "\n"
            return inside
        elif self.contents == []:
            return "nothing"
    def describe(self):
        if self.contents != []:
            print(self.description, "containing:")
            print(self.whats_inside())
        elif hasattr(self, "broken"):
            print(self.description)
        else:
            print(f"{self.description} with {self.whats_inside()} inside.")
    def take_out(self, item, location):
        if self.contents != []:
            self.contents.remove(item)
            location.append(item)
        else:
            raise ValueError

key = Thing(name = "bronze key", description = "A large bronze key.")
rug = Thing(name="rug", description = "An ornate rug.", coveringKey = True, originalSpot = True)
bread = Thing(name = "slice of bread", description = "A slightly stale slice of wheat bread.", edible = True)
sword = Thing(name="glowing sword", description="A glowing sword.")
branch = Thing(name="branch", description="A tree branch.")
jar = Container(name = "jar", description="An empty jar", contents = [], breakable = True)
bottle = Container(name = "bottle", description="A small glass bottle", contents = ["bit of water"])
basket = Container(name= "basket", description="A woven basket", contents = [jar, bottle, "knife"])

class Room():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.contents = []
        self.furniture = []
        self.description = ""
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
        elif item in self.furniture:
            raise AttributeError
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
    def push(self, item):   
        print(f"You move the {item} a couple inches.")
    def update(self):
        pass

class RegularRoom(Room):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.contents = [basket, jar, bottle]
        self.description = "It's just a room."
    def __str__(self):
        return "Regular Room"

class CoolRoom(Room):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.contents = [sword, bread]
    def __str__(self):
        return "Cool Room"
    def update(self):
        if sword in self.contents:
            self.description = "This is a pretty cool room."
        else:
            self.description = "This was a pretty cool room, although you realize it's a lot less cool without the glowing sword."

class StartRoom(Room):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.contents = [branch]
        self.description = "This is the starting room."
    def __str__(self):
        return "Starting Room"

class EmptyRoom(Room):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.contents = []
        self.description = "Just an empty room."
    def __str__(self):
        return "Empty Room"

class RugRoom(Room):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.contents = [sword, bread]
        self.furniture = [rug]
    def __str__(self):
        return "Rug Room"
    def push(self, item):
        if item == rug and rug.originalSpot == True:
            rug.originalSpot = False
            if rug.coveringKey == True:
                self.contents.append(key)
                rug.coveringKey = False
                print("You manage to pull the rug to the side. A large bronze key is laying underneath.")
            else:
                print("You move the rug aside, but nothing is underneath.")
        elif item == rug and rug.originalSpot == False:
            rug.originalSpot = True
            if key in self.contents:
                self.contents.remove(key)
                rug.coveringKey = True
            print("You move the rug back to its original spot.")
        else:
            print(f"You move the {item} a couple inches.")
    def update(self):
        if rug.originalSpot == True and rug.coveringKey == True:
            self.description = "An ornate rug lays on the ground in this room, but it's a bit lumpy."
        if rug.originalSpot == True and rug.coveringKey == False:
            self.description = "An ornate rug lays on the ground in this room."
        elif rug.originalSpot == False:
            self.description = "A rug lays on the ground, slightly askew."

world = [
    [CoolRoom(0,0), CoolRoom(1,0), RegularRoom(2,0)],
    [CoolRoom(0,1), RegularRoom(1,1), StartRoom(2,1)],
    [RugRoom(0,2), EmptyRoom(1,2), RegularRoom(2,2)]
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
                if item != self.contents[0]:
                    inside += "\n"
                if isinstance(item, Container):
                    inside += f"* a {item} which contains: \n"
                    if item.contents == []:
                        inside += '''   nothing'''
                    else:
                        for content in item.contents:
                            if content != item.contents[0]:
                                inside += "\n"
                            inside += f'''   * a {content}'''
                else:
                    inside += f"* a {item}"
            print(inside)
        else:
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
            new_room.update()
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
            if hasattr(item, "edible"):
                self.contents.remove(item)
            else:
                raise AttributeError
        else:
            raise ValueError

player = Player()

item_dict = {
    "key": key,
    "rug": rug,
    "sword": sword,
    "branch": branch,
    "basket": basket,
    "jar": jar,
    "bottle": bottle,
    "bread": bread}

#ALL
all_words = [verb_move, directions, directions_short, verb_inventory, verb_look, verb_examine, word_self, cmd_quit, cmd_help, verb_take, verb_drop, verb_eat, verb_break, verb_push, prep_from, prep_of, articles, item_dict, word_all]

#Checks whether all words are in vocabulary
def check(command):
    if len(command) == 0:
        print("I beg your pardon?")
        return False
    else:
        for command_word in command:
            checker = False
            for word_list in all_words:
                if command_word in word_list:
                    # for debugging: print("I understand", command_word)
                    checker = True
                else:
                    pass
            if checker == False:
                print(f'''I don't know the word "{command_word}".''')
                return False
        if checker == True:
            return True

def parse(command):
    #REMOVE ARTICLES
    command = [word for word in command if word not in articles]
    print(command)
    if command == []:
        print("I'm sorry, I don't understand.")
    #MOVEMENT
    elif any(word in directions for word in command) or any(word in directions_short for word in command) or any(word in verb_move for word in command):
        if command[0] in directions:
            if len(command) == 1:
                player.move_direction(command[0])
            else:
                print(f"I understand you as far as wanting to move {command[0]}.")
        elif command[0] in directions_short:
            command_direction = None
            for direction in directions:
                if command[0] == direction[0]:
                    command_direction = direction
                else:
                    pass
            player.move_direction(command_direction)
        elif command[0] in verb_move:
            if len(command) == 1:
                print(f"Where do you want to {command[0]}?")
            elif len(command) == 2:
                if command[1] in directions or command[1] in directions_short:
                    player.move_direction(command[1])
                else:
                    print(f'"{command[1].capitalize()}" is not a direction.')
            else:
                print(f"I don't understand where you want to {command[0]}.")
        else:
            def is_movement(word):
                return word in directions or word in directions_short or word in verb_move
            desired_direction = [word for index, word in enumerate(command) if is_movement(word)]
            print(f'''I don't understand how you used the word "{desired_direction[0]}".''')
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
                elif command[1] in word_self:
                    player.describe()
                elif item_dict[command[1]] in get_room(player.x, player.y).contents or item_dict[command[1]] in get_room(player.x, player.y).furniture or item_dict[command[1]] in player.contents:
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
            except AttributeError:
                print("That's much too heavy to carry.")
            except ValueError:
                print(f"You don't see a {item} in here.")
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
            print("What do you want to {}?".format(str(command[0])))
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
    #BREAK
    elif command[0] in verb_break:
        def breakit(item):
            try: 
                item_dict[item].breakit(get_room(player.x, player.y).contents)
            except AttributeError:
                print("You hit it as hard as you can, but it doesn't break.")
        if len(command) == 1:
            print(f"What do you want to {command[0]}?")
        elif len(command) == 2:
            breakit(command[1])
        else:
            print(f"I understood you as far as wanting to {command[0]} something.")
    #PUSH
    elif command[0] in verb_push:
        if len(command) == 1:
            print(f"What do you want to {command[0]}?")
        elif len(command) == 2:
            get_room(player.x, player.y).push(item_dict[command[1]])
        else:
            print(f"I understood you as far as wanting to {command[0]} something.")
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
        get_room(player.x, player.y).update()
        command = input(">").lower().split()
        if check(command) == True:
            parse(command)
        print("For debugging: Your coordinates are ({}, {})".format(player.x, player.y))
        print("")

play()


