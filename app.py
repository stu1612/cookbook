import os, math
from flask import Flask, render_template, url_for, request, flash, \
    redirect
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from flask_paginate import Pagination


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
def recipes():
     # Pagination function
    page_limit = 6
    current_page = int(request.args.get('current_page', 1))
    total = mongo.db.recipes.count()
    pages = range(1, int(math.ceil(total / page_limit)) + 1)
    recipes = mongo.db.recipes.find().sort('_id', pymongo.DESCENDING).skip(
                            (current_page - 1)*page_limit).limit(page_limit)
    count = recipes.count()
    return render_template('recipes.html',
                           recipes=recipes, count=count,pages=pages,current_page=current_page,
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
        'tag_1': request.form.get('tag_1'),
        'tag_2': request.form.get('tag_2'),
        'tag_3': request.form.get('tag_3'),
        'prep_time': request.form.get('prep_time'),
        'cook_time': request.form.get('cook_time'),
        'serving': request.form.get('serving'),
        'image': request.form.get('image'),
        'ing_1': request.form.get('ing_1'),
        'ing_2': request.form.get('ing_2'),
        'ing_3': request.form.get('ing_3'),
        'ing_4': request.form.get('ing_4'),
        'ing_5': request.form.get('ing_5'),
        'method_1': request.form.get('method_1'),
        'method_2': request.form.get('method_2'),
        'method_3': request.form.get('method_3'),
        'method_4': request.form.get('method_4'),
        'method_5': request.form.get('method_5'),
        })

    flash('Great - your recipe has been added to our collection !',
          'success')
    return redirect(url_for('recipes'))
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


@app.route('/update_recipe/<recipe_id>', methods=['GET', 'POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update_one({'_id': ObjectId(recipe_id)}, 
    {"$set":
        {'title': request.form.get('title'),
        'tag_1': request.form.get('tag_1'),
        'tag_2': request.form.get('tag_2'),
        'tag_3': request.form.get('tag_3'),
        'prep_time': request.form.get('prep_time'),
        'cook_time': request.form.get('cook_time'),
        'serving': request.form.get('serving'),
        'image': request.form.get('image'),
        'ing_1': request.form.get('ing_1'),
        'ing_2': request.form.get('ing_2'),
        'ing_3': request.form.get('ing_3'),
        'ing_4': request.form.get('ing_4'),
        'ing_5': request.form.get('ing_5'),
        'method_1': request.form.get('method_1'),
        'method_2': request.form.get('method_2'),
        'method_3': request.form.get('method_3'),
        'method_4': request.form.get('method_4'),
        'method_5': request.form.get('method_5')
        }
    })
    flash('The recipe has successfully been updated!', 'success')
    return redirect(url_for('recipes'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove()
    flash('The recipe has been deleted', 'primary')
    return redirect(url_for('recipes'))


@app.route('/post_search', methods=['POST'])
def post_search_food_type():
        recipes=mongo.db.recipes.find()
        search = request.form.get('post_search_food_type')
        post_search_food_type = mongo.db.recipes.find({"tag_2": {"$regex":search}})
        count = post_search_food_type.count()
        return render_template("filtered_search.html", recipes=recipes, post_search_food_type=post_search_food_type, count=count, title="Filtered Search")    
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT'
            )), debug=True)


			