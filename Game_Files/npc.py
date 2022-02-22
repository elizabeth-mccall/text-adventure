import items

class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError("Don't create raw NPC objects!")
    def __str__(self):
        return self.name

class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Trader"
        self.gold = 100
        self.inventory = [items.CrustyBread(), items.CrustyBread(), items.Potion(), items.Potion(), items.Potion(), items.Crossbow()]

        