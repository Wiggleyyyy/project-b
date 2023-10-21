from utils import list_contained

class Dessert:
    def __init__(self, ingredients, sell_price): # these ingredients refer to the ones needed to bake
      self.ingredients = ingredients
      self.amount = 0 # total amount of a type of desserts (like amount of chocolate cakes)
      self.sell_price = sell_price # the money you get back if you want to sell it

    def prepare(self, ingredients_list): # function to prepare the recipe
       if list_contained.first_contains_second(ingredients_list, self.ingredients): # ingredients_list refers to the ingredients the user has
          self.amount = self.amount + 1
          return True # if you have the right ingredients it returns true
       else: return False
      
