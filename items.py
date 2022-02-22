class Weapon:
    def __init__(self):
        raise NotImplementedError("Don't create raw Weapon objects!")
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
