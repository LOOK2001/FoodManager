class food_management:

    def __init__(self):
        pass

    # finds avaliable recipes based on the amount of food in stock
    def findAvaliableRecipe(self, allRecipe, foodList):
        quantityAfterRecipe = {}
        avaliableRecipe = []
        ingredientOfRecipe = {}

        # creates a dictionary of current food in stock and amount
        for currentFood in foodList:
            quantityAfterRecipe[currentFood] = currentFood.getQuantity()
        
        # finds the recipes based on the amount of food in stock
        for currentRecipe in allRecipe:
            hasIngredients = False
            ingredientOfRecipe = currentRecipe.getIngredients()
            for foodItem, quantity in ingredientOfRecipe.items():
                for currentFood in foodList:
                    # if a recipe is found, subtracts its ingredients from current food in stock
                    if foodItem == currentFood and quantityAfterRecipe[foodItem] >= quantity:
                        hasIngredients = True
                        quantityAfterRecipe[currentFood] -= quantity
                        break
                if hasIngredients == False:
                    break
            if hasIngredients == True:    
                avaliableRecipe.append(currentRecipe)
        return avaliableRecipe

    # finds recipes that have or contain the given recipe name
    def findRecipeName(self, allRecipe, name):
        foundRecipe = []
        for currentRecipe in allRecipe:
            if name in currentRecipe.getRecipeName:
                foundRecipe.append(currentRecipe)
        return foundRecipe

    # finds recipes that are equal or lower than set price
    def findPrice(self, allRecipe, price):
        foundRecipe = []
        for currentRecipe in allRecipe:
            if price <= currentRecipe.getTotalPrice:
                foundRecipe.append(currentRecipe)
        return foundRecipe

    # finds recipes for either breakfast, lunch, or dinner
    def findCorrespondingMeal(self, allRecipe, meal):
        foundRecipe = []
        for currentRecipe in allRecipe:
            if meal in currentRecipe.getMealType:
                foundRecipe.append(currentRecipe)
        return foundRecipe

    # finds recipes that contain certain ingredients
    def findCorrespondingIngredients(self, allRecipe, ingredients):
        foundRecipe = []
        hasIngredients = True
        for currentRecipe in allRecipe:
            for ingredientNeeded in ingredients:
                foundIngredient = False
                for recipeIngredient in currentRecipe.getIngredients:
                    if ingredientNeeded == recipeIngredient:
                        foundIngredient = True
                if foundIngredient == False:
                    hasIngredients = False
            if hasIngredients == True:
                foundRecipe.append(currentRecipe)
        return foundRecipe