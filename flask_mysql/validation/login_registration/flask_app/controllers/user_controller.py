from flask import Flask ,render_template, request, redirect,request,flash,session
from flask_app.models.user_model import User
from flask_app import app, bcrypt


#----- Redirect route from '/'-----#
@app.route('/')
def redirectMain ():

    return redirect('/root')

#----- reg and login route -------#
@app.route('/root')
def regLoginPage ():

    return render_template('reg_login.html')

#------ create route -------#
@app.route ('/register', methods=['post'])
def register ():
    # print(request.form)

    if not User.validate(request.form):
        return redirect('/root')

        #---- this hashs our password -----#
    hash = bcrypt.generate_password_hash(request.form['password'])

    data = {
        'first_name' :request.form ['first_name'],
        'last_name' :request.form ['last_name'],
        'email' : request.form ['email'],
        'password' : hash 
    }

    User.create_user(data)
    return redirect('/dashboard')


#-------- route to login---------#
@app.route ('/login', methods=['POST'])
def login():

    logged_in_user = User.validate_login(request.form)

    if not logged_in_user:
        return redirect('/')
    session['uid'] = logged_in_user.id
    # print(request.form)
    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard ():
    if not 'uid' in session:
        flash('ACCESS DENIED')
        return redirect('/')

    return render_template('welcome.html')

#---- this route clears session once i press logout-----#
@app.route('/logout')
def logout ():
    session.clear()
    return redirect ('/')