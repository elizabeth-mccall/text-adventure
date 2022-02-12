# #Weapons before using OOP inheritance
# class Dagger:
#     def __init__(self):
#         self.name = "Dagger"
#         self.description = "A small dagger with some rust." 
#         self.damage = 10
#     def __str__(self):
#         return self.name

# class RustySword:
#     def __init__(self):
#         self.name = "Sword"
#         self.description = "This sword is showing its age, but it still has some fight in it."
#         self.damage = 20
#     def __str__(self):
#         return self.name

# class Crossbow:
#     def __init__(self):
#         self.name = "Crossbow"
#         self.description = "This crossbow can shoot quite a distance."
#         self.damage = 20
#     def __str__(self):
#         return self.name
##########

#Weapons using OOP
class Weapon:
    def __str__(self):
        return self.name

class Rock(Weapon):
    def __init(self):
        self.name = "Rock"
        self.descriptiion = "A fist-sized rock, suitable for bludgeoning."
        self.damage = 5

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