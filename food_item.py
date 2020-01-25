from flask import Flask, escape, requests

class FoodItem:
    name = 'default'
    cal = 30

    def __init__(self, food_name,calories):
        self.name = food_name
        self.cal = calories
