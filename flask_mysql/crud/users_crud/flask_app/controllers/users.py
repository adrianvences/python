#pair programming with jonnie abella
from flask import Flask, render_template, request, redirect
from flask_app import app
# import the class from friend.py
from flask_app.models.usersC import User
@app.route("/")
def home():
    return redirect ("/all_users")

@app.route("/new")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("index.html",users=users)
            
@app.route('/add_users', methods=["POST"])
def add_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/all_users')

@app.route("/all_users")
def all_users():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("users.html",users=users)

@app.route("/user/<int:id>")
def one_user(id):
    # call the get all classmethod to get all friends
    data = {
        'id' : id
    }
    users = User.get_one(data)
    print(users)
    return render_template ("user_one.html",users=users)

@app.route("/edit/<int:id>")
def edit_user(id):
    data = {'id':id}
    user=User.get_one(data)

    return render_template("edit.html", users=user)

@app.route("/edit/<id>/update", methods=['POST'])
def update_userpy(id):
    data={
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
        "id": id
    }
    User.update(data)
    return redirect(f'/user/{id}')

@app.route('/delete/<int:id>')
def delete(id):
    data={
        'id':id
    }
    User.delete_user(data)
    return redirect('/')
