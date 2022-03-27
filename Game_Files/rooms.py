from items import *

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
    def unlock_adjacents(self):
        if hasattr(get_room(self.x, self.y - 1), "locked"):
            get_room(self.x, self.y - 1).unlock_me()
        elif hasattr(get_room(self.x, self.y + 1), "locked"):
            get_room(self.x, self.y + 1).unlock_me()
        elif hasattr(get_room(self.x - 1, self.y), "locked"):
            get_room(self.x - 1, self.y).unlock_me()
        elif hasattr(get_room(self.x + 1, self.y), "locked"):
            get_room(self.x + 1, self.y).unlock_me()
        else:
            print("That room isn't locked.")

###############
#### ROOMS ####
###############

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

class LockedRoom(Room):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.contents = [branch]
        self.description = "A small room."
        self.locked = True
    def __str__(self):
        return "Locked Room"
    def unlock_me(self):
        if self.locked == True:
            self.locked = False
            print("You unlock the door.")
        elif self.locked == False:
            print("The door is already unlocked.")

world = [
    [LockedRoom(0,0), CoolRoom(1,0), RegularRoom(2,0)],
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
