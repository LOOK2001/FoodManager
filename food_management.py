class food_management:
    overallRecipe = []
    foodList = []
    def __init__(self, inputRecipe, inputFoodList):
        self.overallRecipe = inputRecipe
        self.foodList = inputFoodList

    def findAvaliableRecipe(self):
        avaliableRecipe = []
        ingredientOfRecipe = {}
        for currentRecipe in self.overallRecipe:
            hasIngredients = false
            ingredientOfRecipe = currentRecipe.getIngredients
                for currentIngredient in ingredientOfRecipe:
                    for currentFood in self.foodList:
                        if currentIngredient == currentFood
                            hasIngredients = true
                            break
                    if hasIngredients == false
                        break
                if hasIngredients == true       
                      avaliableRecipe.append(currentRecipe)
                        
