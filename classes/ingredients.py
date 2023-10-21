import numpy as np

class Ingredient:
    def __init__(self, price, type, icon): # to identify the ingredient 
        self.price = price # its price
        self.sell_price = (price / 2) # the money you get back if you want to sell it
        self.type = type
        self.icon = icon

    def buy(self, ingredients_list, money): #stil have to figure out how to do ingredients_list
        if money < self.price: return False
        else: return money - self.price, np.append(ingredients_list, [self.type])




"""
how this should go

flour = Ingredient(3, 5)
if button for the flour got clicked,

attempt = flour.buy(ingredients_list)

if attempt == False say that no money to buy
else it will return the new amount of money and the updated ingredients list

"""
