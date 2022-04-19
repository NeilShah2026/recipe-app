from flask import Flask, render_template, request, redirect, url_for
import json
from forms import RecipeForm, SearchForm

app = Flask(__name__)
app.secret_key = 'mysecretkey'
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    # load json file
    with open('recipes.json') as json_file:
        data = json.load(json_file)
    
    # get recipes from json file
    recipes = data['recipes']

    if request.method == 'POST':
        search = form.search.data
        return redirect(url_for('search', search=search))

    return render_template('index.html', recipes=recipes, form=form)

# search recipes
@app.route('/search/<search>', methods=['GET', 'POST'])
def search(search):
    form = SearchForm()

    if request.method == 'POST':
        search = form.search.data
        return redirect(url_for('search', search=search))
        
    # load json file
    with open('recipes.json') as json_file:
        data = json.load(json_file)
    
    # get recipes from json file
    recipes = data['recipes']

    # search recipes
    search_recipes = []
    for recipe in recipes:
        if search.lower() in recipe['title'].lower():
            search_recipes.append(recipe)
    return render_template('search.html', recipes=search_recipes, form=form)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = RecipeForm()
    if request.method == 'POST':
        name = form.title.data
        ingredients = form.ingredients.data
        instructions = form.instructions.data

        # load json file
        with open('recipes.json', 'r') as json_file:
            data = json.load(json_file)
        # add new recipe
        data['recipes'].append({'title': name, 'ingredients': ingredients, 'instructions': instructions})
        # save json file
        with open('recipes.json', 'w') as json_file:
            json.dump(data, json_file)
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
