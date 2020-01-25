from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)             

#initialize controller here, or any models
food = ["apples","wings"]
stock = []

#intialize database to hold food stock, recipes
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

db = SQLAlchemy(app)
class students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))  
   addr = db.Column(db.String(200))
   pin = db.Column(db.String(10))

def __init__(self, name, city, addr,pin):
   self.name = name
   self.city = city
   self.addr = addr
   self.pin = pin

#home page
@app.route("/")                   
def index():
    return render_template("index.html",foods = food, stocks = stock)

#add in item to the grocery list
@app.route('/add', methods=['POST'])
def add_item():
    # get the food and quantity from the grocery form
    new_food = request.form["groceryitem"]
    quan = request.form["quantity"]
    
    food.append(new_food)

    #reload page
    return index()

#add items that were in the grocery list to the food stock
@app.route('/shop', methods=['POST'])
def add_to_stock():
    for item in food:
        stock.append(item)
    food.clear()

    #reload page
    return index()

if __name__ == "__main__":        
    app.run()
