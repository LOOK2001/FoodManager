from flask import Flask

class Recipe:
    ingredients = {}
    meal_name = "meal"
    total_price = 0
    total_weight = 0

    def __init__(self,ingredients,name):
        self.ingredients = ingredients
        self.meal_name = name

    def addItem(self, item, quantity):
        if item in self.ingredients.keys():
            self.ingredients[item] = self.ingredients[item] + quantity
        else:
            self.ingredients[item] = quantity

    def deleteByItem(self, item):
        self.ingredients.remove(item)

    def deleteByIndex(self, index):
        del self.ingredients[index]

    def getTotalCal(self):
        cal = 0
        for item in self.ingredients.keys():
            cal += (item.cal * self.ingredients[item])

        return cal

    def getTotalPrice(self):
        price = 0
        for item in self.ingredients.keys():
            price += (item.price * self.ingredients[item])

        return price



class RecipeList:
    __recipies = []

    def __init__(self,recipies):
        self.__recipies = recipies

    def addRecipe(self, recipe):
        self.__recipies.append(recipe)

    def deleteRecipeByIndex(self, index):
        del self.__recipies[index]

    def deleteRecipeByItem(self, item):
        self.__recipies.remove(item)

    def getRecipies(self):
        return self.__recipies

class FoodList:
    __Foodlist = []

    def __init__(self,food):
        self.__Foodlist = food

    def addFood(self, foodItem):
        self.__Foodlist.append(foodItem)

    def deleteFoodByIndex(self, index):
        del self.__Foodlist[index]

    def deleteFoodByItem(self, foodItem):
        self.__Foodlist.remove(foodItem)

    def getFoodList(self):
        return self.__Foodlist