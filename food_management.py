class food_management:
    allRecipe = []
    foodList = []
    def __init__(self, inputRecipe, inputFoodList):
        self.overallRecipe = inputRecipe
        self.foodList = inputFoodList

    def findAvaliableRecipe(self):
        avaliableRecipe = []
        ingredientOfRecipe = {}
        for currentRecipe in self.allRecipe:
            hasIngredients = False
            ingredientOfRecipe = currentRecipe.getIngredients()
            for foodItem, quantity in ingredientOfRecipe.items():
                for currentFood in self.foodList:
                    if foodItem == currentFood:
                        hasIngredients = True
                        break
                if hasIngredients == False:
                    break
            if hasIngredients == True:    
                avaliableRecipe.append(currentRecipe)
                        
