class food_management:
    overallRecipe = []
    def __init__(self, inputRecipe):
        self.overallRecipe = inputRecipe

    def findAvaliableRecipe(self):
        ingredients = {}
        for x in self.overallRecipe:
            ingredients = x.getIngredients

