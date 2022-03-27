###############
#### ITEMS ####
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
