import os
from flask import Flask, render_template, url_for, request, flash, \
    redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'cook_book'
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/recipes')
def recipes_page():
    return render_template('recipes.html',
                           recipes=mongo.db.recipes.find(),
                           title='Recipes')


@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html', title='Create Recipe',
                           recipes=mongo.db.recipes.find())


@app.route('/post_recipe', methods=['POST'])
def post_recipe():
    if request.method == 'POST':
        recipes = mongo.db.recipes
    recipes.insert({
        'title': request.form.get('title'),
        'tags': [{'tag': request.form.get('tag_1')},
                 {'tag': request.form.get('tag_2')},
                 {'tag': request.form.get('tag_3')}],
        'prep_time': request.form.get('prep_time'),
        'cook_time': request.form.get('cook_time'),
        'serving': request.form.get('serving'),
        'image': request.form.get('image'),
        'ingredients': [{'ing': request.form.get('ing_1'),
                        'qty': request.form.get('qty_1')},
                        {'ing': request.form.get('ing_2'),
                        'qty': request.form.get('qty_2')},
                        {'ing': request.form.get('ing_3'),
                        'qty': request.form.get('qty_3')},
                        {'ing': request.form.get('ing_4'),
                        'qty': request.form.get('qty_4')},
                        {'ing': request.form.get('ing_5'),
                        'qty': request.form.get('qty_5')}],
        'methods': [{'method': request.form.get('method_1')},
                    {'method': request.form.get('method_2')},
                    {'method': request.form.get('method_3')},
                    {'method': request.form.get('method_4')},
                    {'method': request.form.get('method_5')}],
        })

    flash('Great - your recipe has been added to our collection !',
          'success')
    return redirect(url_for('recipes_page'))
# return render_template('add_recipe.html', title='Create Recipe')


# the_recipe route is the route to see the selected card recipe in a full html page including all contents

@app.route('/the_recipe/<recipe_id>')
def the_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find({'_id': ObjectId(recipe_id)})
    return render_template('the_recipe.html', title='Selected Recipe',
                       recipes=the_recipe)


# update_recipe route is the route to see the returned selected recipe_id to edit contents

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('update_recipe.html', recipe=the_recipe,
                       title='Update Recipe')


@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)}, {
    'title': request.form.get('title'),
    'tags': [{'tag': request.form.get('tag_1')},
             {'tag': request.form.get('tag_2')},
             {'tag': request.form.get('tag_3')}],
    'prep_time': request.form.get('prep_time'),
    'cook_time': request.form.get('cook_time'),
    'serving': request.form.get('serving'),
    'image': request.form.get('image'),
    'ingredients': [{'ing': request.form.get('ing_1'),
                    'qty': request.form.get('qty_1')},
                    {'ing': request.form.get('ing_2'),
                    'qty': request.form.get('qty_2')},
                    {'ing': request.form.get('ing_3'),
                    'qty': request.form.get('qty_3')},
                    {'ing': request.form.get('ing_4'),
                    'qty': request.form.get('qty_4')},
                    {'ing': request.form.get('ing_5'),
                    'qty': request.form.get('qty_5')}],
    'methods': [{'method': request.form.get('method_1')},
                {'method': request.form.get('method_2')},
                {'method': request.form.get('method_3')},
                {'method': request.form.get('method_4')},
                {'method': request.form.get('method_5')}],
    })

    flash('Your updates have been successfully made', 'success')
    return redirect(url_for('recipes'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT'
            )), debug=True)


			