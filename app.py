import os
from flask import Flask, render_template, url_for, request, flash, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)
# app.config["MONGO_DBNAME"] = 'recipe_collection'
# app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.secret_key = "key"


recipes = [{
        'title': 'Italien Lasagna with chorizo, feta cheese and spinach',
        'ingredients': 'Mince, Onion, Pasta sheets',
        'instructions': 'Cook carefully',
        'categories': 'Meat, Italien, Lasagna, Pasta',
        'cook_time': '1.5 hrs',
        'preperation_time': '30 mins',
        'date_posted': 'December 03, 2019'
    },
    {
        'title': 'Sausage Pasta',
        'ingredients': 'Sausage, pasta, white sauce',
        'instructions': 'Cook carefully',
        'categories': 'Meat, Pasta',
        'cook_time': '30 mins',
        'preperation_time': '5 mins',
        'date_posted': 'December 02, 2019'
    },
    {
        'title': 'Sausage Pasta',
        'ingredients': 'Sausage, pasta, white sauce',
        'instructions': 'Cook carefully',
        'categories': 'Meat, Pasta',
        'cook_time': '30 mins',
        'preperation_time': '5 mins',
        'date_posted': 'December 02, 2019'
    },
    {
        'title': 'Salad',
        'ingredients': 'Sausage, pasta, white sauce',
        'instructions': 'Cook carefully',
        'categories': 'Meat, Pasta',
        'cook_time': '30 mins',
        'preperation_time': '5 mins',
        'date_posted': 'December 02, 2019'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/recipes')
def recipes_page():
    return render_template('recipes.html', recipes=recipes, title='Recipes')
    
    
@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        flash('Great - your recipe has been added to our collection !', 'success')
        return redirect(url_for('recipes_page'))
    return render_template('add_recipe.html', title='Create Recipe')
    
    
@app.route('/post_recipe')
def post_recipe():
    return render_template('add_recipe.html', title='Create Recipe')    


if __name__ == '__main__':
    app.run(host = os.environ.get('IP'),
        port = int(os.environ.get('PORT')),
        debug = True)