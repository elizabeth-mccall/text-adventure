import world

class Player():
    def __init__(self):
        self.inventory = []
        self.x = world.start_location[0]
        self.y = world.start_location[1]
    def move(self, dx, dy):
        old_x = self.x
        old_y = self.y
        self.x += dx
        self.y += dy
        new_room = world.tile_at(self.x, self.y)
        if new_room == None:
            print("You can't go that way.")
            self.x = old_x
            self.y = old_y
        else:
            print(new_room)
            if new_room.visited == False:
                print(new_room.description())
                new_room.mark_visited()
            else:
                pass
    def move_north(self):
        self.move(dx = 0, dy = -1)
    def move_south(self):
        self.move(dx = 0, dy = 1)
    def move_east(self):
        self.move(dx = 1, dy = 0)
    def move_west(self):
        self.move(dx = -1, dy = 0)
