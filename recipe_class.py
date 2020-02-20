# Create a Recipe class

class Recipe:

    def __init__(self, name, ingredients, instructions, calorie_count=None):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        if calorie_count is None:  # Set default cc to None in case its not available / not calculated yet
            self.calorie_count = {}
        else: 
            self.calorie_count = calorie_count
    def __repr__(self):
        return "Recipe:\n '{}',\n '{}',\n '{}',\n '{}' ".format(self.name, self.ingredients, self.instructions, self.calorie_count)

# Add a Subclass for Baked Goods to account for oven settings and bake time

class Baked_Goods(Recipe):

    def __init__(self, name, ingredients, instructions, heat, oven_setting, bake_time, calorie_count=None):
        super().__init__(name, ingredients, instructions)
        self.heat = str(heat) + " Degrees"
        self.oven_setting = oven_setting
        self.bake_time = str(bake_time) + " Minutes"
        if calorie_count is None:
            self.calorie_count = {}
        else: 
            self.calorie_count = calorie_count

    def __repr__(self):
        return "Recipe:\n '{}',\n '{}',\n '{}',\n '{}',\n '{}',\n '{}',\n '{}' ".format(self.name, self.ingredients, self.instructions, self.heat, self.oven_setting, self.bake_time, self.calorie_count)
    

# Some test objects go here


crepes = Recipe("Crêpes",
    {"Flour": "150g",
    "Eggs": "1",
    "Milk": "100ml"},
    "Mix ingredients, pour 1 ladle at a time into pan, flip after 30 seconds",
    {"Fat": "20g", "Protein": "5g", "Carbs": "40g"})

#print(crepes.ingredients)
#print(crepes.instructions)
#print(crepes.calorie_count)
