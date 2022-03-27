from rooms import *

###############
#### PLAYER ###
###############

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
            return inside
        else:
            return "\n nothing"
    def inventory(self):
        print(f"You are carrying: {self.whats_inside()}")
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
        elif hasattr(new_room, "locked"):
            if new_room.locked == True:
                self.x = old_x
                self.y = old_y
                print("The door is locked, preventing you from going in.")
            elif new_room.locked == False:
                print(new_room)
                new_room.update()
                new_room.describe()
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