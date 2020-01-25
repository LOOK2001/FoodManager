from flask import Flask, escape, requests

class FoodItem:
    name = 'default'
    cal = 30
    price = 0

    def __init__(self, food_name,calories, price):
        self.name = food_name
        self.cal = calories
        self.price = price
