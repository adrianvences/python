from flask_app import app,bcrypt
from flask_app.models.user_model import User
from flask_app.models.recipes_model import Recipe
from flask import Flask , render_template,request, redirect, request,flash,session



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/edit')
def edit():
    return render_template('edit.html')


#------ create route -------#
@app.route ('/register', methods=['post'])
def register ():
    # print(request.form)

    if not User.validate(request.form):
        return redirect('/')

        #---- this hashs our password -----#
    hash = bcrypt.generate_password_hash(request.form['password'])

    new_user = {
        'first_name' :request.form ['first_name'],
        'last_name' :request.form ['last_name'],
        'email' : request.form ['email'],
        'password' : hash 
    }
    #--- had to turn this into create var----# 
    #--- then use session to pull uid from create---#
    create = User.create_user(new_user)

    session['uid'] = create

    return redirect('/recipes')

#-------- route to login---------#
@app.route ('/login', methods=['POST'])
def login():

    logged_in_user = User.validate_login(request.form)

    if not logged_in_user:
        return redirect('/')
    session['uid'] = logged_in_user.id
    # print(request.form)
    return redirect('/recipes')


@app.route('/logout')
def logout ():
    session.clear()
    return redirect ('/')