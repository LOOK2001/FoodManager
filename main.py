from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from food_item import FoodItem
from recipe_form import RecipeForm
import os
SECRET_KEY = os.urandom(32)


app = Flask(__name__)             
app.config['SECRET_KEY'] = SECRET_KEY
#initialize controller here, or any models
grocery_list = []

#intialize database to hold food stock, recipes
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

#create database and table
db = SQLAlchemy(app)

class Recipe_Item(db.Model):
   id = db.Column('recipe_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   ingredient = db.Column(db.String(100))

   def __init__(self,name,ing):
       self.name = name
       self.ingredient = ing
       
class Food_Item(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   quantity = db.Column(db.Integer)

   def __init__(self,name,quan):
       self.name = name
       self.quantity = quan
#initialize table
db.create_all()

#home page
@app.route("/")                   
def index():
    stock = Food_Item.query.all()
    return render_template("index.html",foods = grocery_list, stocks = stock)

#add in item to the grocery list
@app.route('/add', methods=['POST'])
def add_item():
    #create a food item obj
    new_food = Food_Item(request.form["groceryitem"],int(request.form["quantity"]))
    # get the food and quantity from the grocery form

    #add food grocery list
    grocery_list.append(new_food)

    #reload page
    return index()

#add items that were in the grocery list to the food stock
@app.route('/shop', methods=['POST'])
def add_to_stock():
    #loop through grocery list and add to db
    for item in grocery_list:
        food_item = Food_Item(item.name,item.quantity)
        # check if its in the db alrady, update if so
        all_food = Food_Item.query.all()
        found = False
        # CANT QUERY ITS BEING WEIRD, using loop for now
        for food in all_food:
            if food.name == item.name:
                food.quantity += item.quantity
                found = True
        #if food not in database, add a new entry
        if(found == False):
            db.session.add(food_item)
        
    # clear the grocery list
    grocery_list.clear()
    db.session.commit()
    #reload page
    return index()

#adds a recipe item
@app.route('/recipe_form',methods=["POST","GET"])
def recipe_form():
    meal_list = Recipe_Item.query.all()
    if request.method == 'GET':
        form = RecipeForm()
    else:
        new_recipe = Recipe_Item(request.form["meal_name"],request.form["ingredient"])
        db.session.add(new_recipe)
        db.session.commit()
    return render_template("recipeui.html",form=form,meals=meal_list)

#removes a food item
@app.route('/remove_food',methods=["POST"])
def remove_food():
    Food_Item.query.filter_by(name = request.form["groceryitem"]).delete()
    db.session.commit()
    return index()

#generates a meal plan
@app.route('/meal_plan',methods=["POST", "GET"])
def generate_plan():
    if request.method == "GET":
        return index()

if __name__ == "__main__":        
    app.run()
