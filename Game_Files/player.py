import world

class Player():
    def __init__(self):
        self.inventory = []
        self.x = world.start_location[0]
        self.y = world.start_location[1]
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def move_north(self):
        self.move(dx = 0, dy = -1)
    def move_south(self):
        self.move(dx = 0, dy = 1)
    def move_east(self):
        self.move(dx = 1, dy = 0)
    def move_west(self):
        self.move(dx = -1, dy = 0)
