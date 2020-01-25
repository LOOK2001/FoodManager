from flask import Flask
import food_item

class Recipe:
    ingredients = []
    meal_name = "meal"

    def __init__(self,ingredients,name):
        self.ingredients = ingredients
        self.meal_name = name

class RecipeList:
    recipies = []

    def __init__(self,recipies):
        self.recipies = recipies
