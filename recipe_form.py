from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RecipeForm(FlaskForm):
    meal_name = StringField("Recipe Name")
    ingredient = StringField("Ingredient")
    submit = SubmitField("Add Recipe")
