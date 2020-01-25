class food_management:

    def __init__(self):
        pass

    def findAvaliableRecipe(self, allRecipe, foodList):
        quantityAfterRecipe = {}
        avaliableRecipe = []
        ingredientOfRecipe = {}
        for currentFood in foodList:
            quantityAfterRecipe[currentFood] = currentFood.getQuantity()
        
        for currentRecipe in allRecipe:
            hasIngredients = False
            ingredientOfRecipe = currentRecipe.getIngredients()
            for foodItem, quantity in ingredientOfRecipe.items():
                for currentFood in foodList:
                    if foodItem == currentFood and quantityAfterRecipe[foodItem] >= quantity:
                        hasIngredients = True
                        quantityAfterRecipe[currentFood] -= quantity
                        break
                if hasIngredients == False:
                    break
            if hasIngredients == True:    
                avaliableRecipe.append(currentRecipe)
        return avaliableRecipe

    def findRecipeName(self, allRecipe, name):
        foundRecipe = []
        for currentRecipe in allRecipe:
            if