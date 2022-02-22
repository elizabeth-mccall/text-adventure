import enemies
import random

class MapTile:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")
    def modify_player(self, player):
        pass

#To do later: change the text 
class StartTile(MapTile):
    def intro_text(self):
        return '''
        You find yourself in a case with a flickering torch on the wall. 
        You can make out four paths, each equally as dark and foreboding.
        '''

class BoringTile(MapTile):
    def intro_text(self):
        return '''
        This is a very boring part of the cave.
        '''

class VictoryTile(MapTile):
    def intro_text(self):
        return '''
        You see a bright light in the distance...
        ... it grows closer as you get closer! It's sunlgiht! 
        
        Victory is yours!'''

class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.5:
            self.enemy = enemies.GiantSpider()
            self.alive_text = "A giant spider jumps down from its web in front of you!"
            self.dead_text = "The corpse of a dead spider rots on the ground."
        elif r < 0.8:
            self.enemy = enemies.Ogre()
            self.alive_text = "An ogre is blocking your path!"
            self.dead_text = "A dead ogre reminds you of your triumph."
        elif r < 0.95:
            self.enemy = enemies.BatColony()
            self.alive_text = "You hear squeaking noises growing louder... suddenly you're lost in a swarm of bats!"
            self.dead_text = "Dozens of dead bats litter the ground."
        else:
            self.enemy = enemies.RockMonster()
            self.alive_text = "You've disturbed a rock monster from its slumber!"
            self.dead_text = "Defeated, the monster has reverted into an ordinary rock."
        super().__init__(x, y)
    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text
    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("The {} does {} damage. You have {} HP remaining.".format(self.enemy.name, self.enemy.damage, player.hp))

#Creates a "Domain Specific Language" (DSL) for the world map. The DSL is initially just a string, and code needs to be written to let Python "understand"/parse it
world_dsl = '''
|  |VT|  |
|  |EN|  |
|EN|ST|  |
|  |EN|  |
'''

#Checks whether the DSL is "valid" (i.e., was it written correctly). Returning False will raise an error later
def is_dsl_valid(dsl):
    #if there isn't 1 start tile, returns False
    if dsl.count("|ST|") != 1:
        return False
    #if there isn't a victory tile, returns False
    if dsl.count("|VT|") == 0:
        return False
    #splits the map line by line
    lines = dsl.splitlines()
    #removes the empty top line
    lines = [l for l in lines if l]
    #counts the number of | in each line
    pipe_counts = [line.count("|") for line in lines]
    #if the number of | don't match up, returns False
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False
    return True

#Matches tile names in DSL to MapTile types
tile_type_dict = {"VT": VictoryTile,
                  "EN": EnemyTile,
                  "ST": StartTile,
                  "  ": None}
        
world_map = []

#Gives Python rules for understanding the DSL
def parse_world_dsl():
    #checks validity - if False, raises error
    if not is_dsl_valid(world_dsl):
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
            #replaces cells with appropriate MapTile objects & pass in x-y coordinates
            tile_type = tile_type_dict[dsl_cell]
            row.append(tile_type(x, y) if tile_type else None)
        #adds row to world map - now world map is a list of lists, made out of MapTiles & None types
        world_map.append(row)

def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None

