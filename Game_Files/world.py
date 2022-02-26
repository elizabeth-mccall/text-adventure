#Creates the Room class (all rooms are based on this class)
class Room():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def description(self):
        raise NotImplementedError("Make a subclass first!")
    def modify_player(self, player):
        pass

#Starting room
class StartingRoom(Room):
    def __str__(self):
        return "Damp Cell"
    def description(self):
        return "The floors of this dark cell pool with dirty water. A tiny window in the wall lets in a sliver of light. An iron door leads north."

class JustaRoom(Room):
    def __str__(self):
        return "Just a Room"
    def description(self):
        return "It's just a regular old room."

# **** Following DSL pretty much from textbook ****
world_dsl = '''
|RM|RM|RM|
|RM|RM|RM|
|RM|ST|RM|
|RM|RM|RM|
'''

#Dictionary for room name/types
room_type_dict = {"RM": JustaRoom,
                  "ST": StartingRoom,
                  "  ": None}

#Checks whether world map is "valid" (i.e., was it written correctly). Returning False will raise an error later
def is_dsl_valid(world_dsl):
    #if there isn't 1 start tile, returns False
    if world_dsl.count("|ST|") != 1:
        return False
    #splits the map line by line
    lines = world_dsl.splitlines()
    #removes the empty top line
    lines = [l for l in lines if l]
    #counts the number of | in each line
    pipe_counts = [line.count("|") for line in lines]
    #if the number of | don't match up, returns False
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False
    return True

#Creates empty world map
world_map = []

start_location = None

#Gives Python rules for understanding the DSL
def parse_world_dsl():
    #checks validity - if False, raises error
    if is_dsl_valid(world_dsl) == False:
        raise SyntaxError("World Map DSL is invalid!")
    #splits map line by line
    dsl_lines = world_dsl.splitlines()
    #removes empty top line
    dsl_lines = [x for x in dsl_lines if x]
    #iterates through each row in the map
    for y, dsl_row in enumerate(dsl_lines):
        row = []
        #splits rows into cells
        dsl_cells = dsl_row.split("|")
        #removes empty cells
        dsl_cells = [c for c in dsl_cells if c]
        #iterates over each cell in the row
        for x, dsl_cell in enumerate(dsl_cells):
            #replaces cells with appropriate Room objects & pass in x-y coordinates
            room_type = room_type_dict[dsl_cell]
            #separate rule for StartingRoom
            if room_type == StartingRoom:
                global start_location
                start_location = x, y
            row.append(room_type(x, y) if room_type else None)
        #adds row to world map - now world map is a list of lists, made out of Rooms & None types
        world_map.append(row)

def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
