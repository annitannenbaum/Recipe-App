# Four tables and therefore four classes are needed
# First, we create the basis for our recipes

class Recipe_Basis:
    def __init__(self, basic_id, name, instructions):
        self.id = id
        self.name = name
        self.instructions = instructions
    def __repr__(self):
        return "Recipe Basis: \n ID: '{}', \n Name: '{}', \n Instructions: '{}'".format(self.id, self.name, self.instructions)

# A table for ingredients with a Foreign Key to link to other tables

class Ingredients:
    def __init__(self, ig_id, ingredient):
        self.ig_id = ig_id
        self.ingredient = ingredient
    def __repr__(self):
        return "Ingredients: \n Ingredient ID: '{}', \n Ingredient Name: '{}'".format(self.ig_id, self.ingredient)

# A table for ingredient quantities

class Quantities:
    def __init__(self, qu_id, quantity):
        self.qu_id = qu_id
        self.quantity = quantity
    def __repr__(self):
        return "Quantities: \n Quantity ID: '{}', \n Quantity Name: '{}'".format(self.qu_id, self.quantity)

# An optional settings class for baking recipes

class Settings_Baking:
    def __init__(self, set_id, heat, bake_time, oven_setting):
        self.set_id = set_id
        self.heat = heat
        self.bake_time = bake_time
        self.oven_setting = oven_setting
    def __repr__(self):
        return "Baking Settings: \n Setting ID: '{}', \n Heat: '{}', \n Bake Time: '{}', \n Oven Setting: '{}'".format(self.set_id, self.heat, self.bake_time, self.oven_setting)

# Another optional class for the calorie count

class Calorie_Count:
    def __init__(self, cc_id, carbs, fat, protein):
        self.cc_id = cc_id
        self.carbs = carbs
        self.fat = fat
        self.protein = protein
    def __repr__(self):
        return "Calorie Count: \n Calorie Count ID: '{}', \n Carbohydrates: '{}', \n Fat: '{}', \n Protein: '{}'".format(self.cc_id, self.carbs, self.fat, self.protein)

