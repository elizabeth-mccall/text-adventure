class Food: 
    def __init__(self, name, carbs, protein, fat):
        self.name = name
        self.carbs = carbs
        self.protein = protein
        self.fat = fat
    def calories(self):
        return (self.carbs * 4) + (self.protein * 4) + (self.fat * 9)
    def __str__(self):
        return self.name

class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
    def calories(self):
        total = 0
        for each_food in self.ingredients:
            total = total + each_food.calories()
        return total
    def __str__(self):
        return self.name 

pesto_pasta = Recipe("Pesto Pasta", [Food(name="pasta", carbs=6, protein=8, fat=12), Food(name="pesto", carbs=2, protein=2, fat=10), Food(name="butter", carbs=4,protein=5,fat=16)])

scrambled_eggs = Recipe("Scrambled Eggs", [Food(name="egg", carbs=4, protein=20, fat=10), Food(name="salt", carbs=0, protein=0, fat=0), Food(name="butter", carbs=4,protein=5,fat=16)])

recipes = [pesto_pasta, scrambled_eggs]

for each_recipe in recipes:
    print("-" * 20, "\n {}: {} calories".format(each_recipe.name, each_recipe.calories()))
    for each_ingredient in each_recipe.ingredients:
        print("*", (each_ingredient.name).capitalize())


