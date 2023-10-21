from classes import ingredients, recipes

# icons to change once they are done
all_ingredients_available = [
    ingredients.Ingredient(200, 0, "icon"), # flour 
    ingredients.Ingredient(300, 1, "icon"), # sugar
    ingredients.Ingredient(200, 2, "icon"), # egg pack
    ingredients.Ingredient(350, 3, "icon"), # chocolate 
    ingredients.Ingredient(200, 4, "icon"), # flour 
    ingredients.Ingredient(50, 5, "icon"), # baking powder 
    ingredients.Ingredient(600, 6, "icon"), # honey 
    ingredients.Ingredient(400, 7, "icon"), # heavy cream 
    ingredients.Ingredient(10, 8, "icon"), # water 
    ]

all_recipes_available = [
    recipes.Dessert([0, 8], 30) # bread, as you can see, the ingredients required to bake bread are water and flour (8 and 0)
]