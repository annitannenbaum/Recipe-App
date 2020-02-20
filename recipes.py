### Import modules

import sqlite3
import recipe_classes_reviewed

### Connect to database

conn = sqlite3.connect(":memory:")

c = conn.cursor()

### Create necessary tables from imported classes

c.execute("""CREATE TABLE IF NOT EXISTS recipe_basis (
    recipe_id integer,
    recipe_name text,
    recipe.instructions text
)""")


c.execute("""CREATE TABLE IF NOT EXISTS ingredients (
    ig_id integer,
    ingredient text
)""")

c.execute(""" CREATE TABLE IF NOT EXISTS quantities (
    qu_id integer,
    quantity text
)""")

c.execute("""CREATE TABLE IF NOT EXISTS settings_baking (
    set_id integer,
    heat integer,
    bake_time integer,
    oven_setting text
)""")

c.execute("""CREATE TABLE IF NOT EXISTS calorie_count (
    cc_id integer,
    carbs integer,
    fat integer,
    protein integer
)""")

### Add new data

def insert_recipe_basis(Recipe_Basis):
    with conn:
        c.execute("INSERT INTO recipe_basis VALUES (:id, :name, :instructions)",
        {"id": Recipe_Basis.id,
        "name": Recipe_Basis.name,
        "instructions": Recipe_Basis.instructions})

def insert_ingredient(Ingredients):
    with conn:
        c.execute("INSERT INTO ingredients VALUES (:ig_id, :ingredient)",
        {"ig_id": Ingredients.ig_id,
        "ingredient": Ingredients.ingredient})

def insert_quantity(Quantities):
    with conn:
        c.execute("INSERT INTO quantities VALUES (:qu_id, :quantity)",
        {"qu_id": Quantities.qu_id,
        "quantity": Quantities.quantity})

def insert_settings_baking(Settings_Baking):
    with conn:
        c.execute("INSERT INTO settings_baking VALUES (:set_id, :heat, :bake_time, oven_setting)",
        {"set_id": Settings_Baking.set_id,
        "heat": Settings_Baking.heat,
        "bake_time": Settings_Baking.bake_time,
        "oven_setting": Settings_Baking.oven_setting})

def insert_calorie_count(Calorie_Count):
    with conn:
        c.execute("INSERT INTO calorie_count VALUES (:cc_id, :carbs, :fat, :protein)",
        {"cc_id": Calorie_Count.cc_id,
        "carbs": Calorie_Count.carbs,
        "fat": Calorie_Count.fat,
        "protein": Calorie_Count.protein})

### Delete existing data

def delete_recipe_basis(Recipe_Basis):
    with conn:
        c.execute("DELETE from recipe_basis WHERE name = :name",
        {"name": Recipe_Basis.name})

def delete_ingredient(Ingredients):
    with conn:
        c.execute("DELETE from ingredients WHERE ingredient = :ingredient",
        {"ingredient": Ingredients.ingredient})

def delete_calorie_count(Calorie_Count):
    with conn:
        c.execute("DELETE from calorie_count WHERE cc_id = :cc_id",
        {"cc_id": Calorie_Count.cc_id})


# bananabread = Baked_Goods("Banana Bread",
#     {"Bananas, very ripe": 3,
#     "Egg": 1,
#     "Vanilla Sugar":"1 Package",
#     "Sugar": "100g",
#     "Flour": "180g",
#     "Salt": "1 Pinch",
#     "Baking Powder": "1 Package",
#     "Chocolate Splinters":
#     "1 Package"},
#     "Puree bananas thoroughly in a bowl. Add egg, sugar and vanilla sugar. Combine dry except for the chocolate and mix with banana-puree. Carefully add chocolate splinters. Line a loaf pan with a baking sheet and pour in mixture",
#     180,
#     "Top- and lower heat",
#     40)



# c.execute('INSERT INTO recipes_baking VALUES (?, ?, ?, ?, ?, ?, ?)',
#     (bananabread.name, bananabread.ingredients, bananabread.instructions, bananabread.heat, bananabread.oven_setting, bananabread.bake_time, None))

conn.commit()