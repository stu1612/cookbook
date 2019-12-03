import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

recipes = [{
        'title': 'Lasagna',
        'description': 'Italien favourite',
        'ingredients': 'Mince, Onion, Pasta sheets',
        'instructions': 'Cook carefully',
        'categories': 'Meat, Italien, Pasta',
        'cook_time': '1.5 hrs',
        'preperation_time': '30 mins',
        'date_posted': 'December 03, 2019'
    },
    {
        'title': 'Salad',
        'description': 'Sausage Pasta',
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
    
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html', title='Create Recipe')


if __name__ == '__main__':
    app.run(host = os.environ.get('IP'),
        port = int(os.environ.get('PORT')),
        debug = True)