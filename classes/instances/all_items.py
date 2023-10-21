from classes import ingredients, recipes

# icons to change once they are done
all_ingredients_available = [
    ingredients.Ingredient(200, "flour", "icon"), # flour 
    ingredients.Ingredient(300, "sugar", "icon"), # sugar
    ingredients.Ingredient(200, "eggs", "icon"), # egg pack
    ingredients.Ingredient(350, "chocolate", "icon"), # chocolate 
    ingredients.Ingredient(200, "vanilla", "icon"), # vanilla
    ingredients.Ingredient(50, "baking_powder", "icon"), # baking powder 
    ingredients.Ingredient(600, "honey", "icon"), # honey 
    ingredients.Ingredient(400, "heavy_cream", "icon"), # heavy cream 
    ingredients.Ingredient(10, "water", "icon"), # water 
    ]

all_recipes_available = [
    recipes.Dessert(["flour", "water"], 30, "icon") # bread, as you can see, the ingredients required to bake bread are water and flour (8 and 0)
]