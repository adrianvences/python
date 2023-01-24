from flask_app import app
from flask_app.models.recipes_model import Recipe
from flask_app.models.user_model import User
from flask import render_template,request,redirect,session,flash


#-------------- Home page -------------#
@app.route('/recipes')
def recipes():
    if not 'uid' in session:
        flash('please login first!')
        return redirect('/')

    logged_in_user = User.find_by_user(session['uid'])

    # all_recipes = Recipe.get_all()

    recipes_with_users = Recipe.get_all_with_users()

    return render_template('recipes.html', user= logged_in_user, recipes=recipes_with_users)





#----------- create recipe -------------#
@app.route('/new_recipe')
def new_recipes():

    if 'uid' not in session:
        return redirect('/')

    logged_in_user = User.find_by_user(session['uid'])

    return render_template('newrecipe.html',user= logged_in_user)

# ---- this actually creates the recipe -----#
@app.route ('/create_recipe', methods = ['POST'])
def create_recipe():

    if not Recipe.validate_recipes(request.form):
        return redirect('/new_recipe')

    new_recipe = {
        'name' :request.form ['name'],
        'description' :request.form ['description'],
        'instructions' : request.form ['instructions'],
        'date_cooked' : request.form ['date_cooked'],
        'under_30' : request.form ['under_30'],
        'user_id' : session ['uid'] 
    }

    #--- had to turn this into create var----# 
    #--- then use session to pull uid from create---#
    create = Recipe.add_recipe(new_recipe)
    print(request.form)
    return redirect ('/recipes')





#------------ edit recipe ------------#
@app.route('/edit_recipe/<int:recipe_id>')
def edit_recipes(recipe_id):


    if 'uid' not in session:
        flash('please login')
        return redirect('/')

    logged_in_user = User.find_by_user(session['uid'])
    recipe = Recipe.find_by_recipe(recipe_id)

    return render_template('edit.html',recipe=recipe, user = logged_in_user)

@app.route ('/save_recipe', methods = ['POST'])
def save_recipe():
    if not Recipe.validate_recipes(request.form):
        return redirect(f'/edit_recipe/{request.form["id"]}')

    Recipe.edit(request.form)
    print(request.form)
    return redirect ('/recipes')






#------- deleting recipe -------#
@app.route ('/delete/recipe/<int:id>')
def delete_recipe(id):
    data = {
        'id':id
    }
    Recipe.delete(data)
    print('this recipe is deleted')
    return redirect('/recipes')


#------- this shows individual recipes ------#
@app.route('/recipe/show/<int:recipe_id>')
def show_recipes(recipe_id):
    if not 'uid' in session:
        flash('please login first')
        return redirect('/')

    logged_in_user = User.find_by_user(session['uid'])
    recipes_with_users = Recipe.find_one_user_by_recipe({'id':recipe_id})
    # print('---------->>>>>>>>>>>',recipes_with_users)
    return render_template('show_recipe.html',user= logged_in_user,users_recipe=recipes_with_users)