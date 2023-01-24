from flask import Flask ,render_template ,request,redirect
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojos

#----------- new ninjas form page -----------#
from flask_app import app 
@app.route('/new_ninjas')
def NinjaPage (): 
    dojos = Dojos.get_all() 
    return render_template('new_ninjas.html',dojos=dojos)

#------ route for when ninjas form is submitted --------#
@app.route("/new_ninjas_form", methods = ["POST"])
def create():
    # data={
    #     'first_name' : request.form ['first_name'],
    #     'last_name' : request.form ['last_name'],
    #     'age' : request.form ['age']
    # }
    new_ninja = Ninja.create(request.form) #since we used req.form 
    dojo_id = request.form['dojo_id']
    # print ("------------------------->", dojo_id)
    return redirect(f'/dojo/{dojo_id}')