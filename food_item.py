class FoodItem:
    name = 'default'
    cal = 0
    price = 0
    quantity = 0

    def __init__(self, food_name,calories, price, quantity):
        self.name = food_name
        self.cal = calories
        self.price = price
        self.quantity = quantity

    def setFoodName(self, name):
        self.name = name

    def setCalories(self, calories):
        self.calories = calories

    def setPrice(self, price):
        self.price = price

    def setQuantity(self, quantity):
        self.quantity = quantity
    
    def getQuantity(self):
        return self.quantity

    def getCal(self):
        return self.cal

    def getPrice(self):
        return self.price

    def getName(self):
        return self.name