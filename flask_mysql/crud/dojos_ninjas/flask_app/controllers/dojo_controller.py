from flask import Flask ,render_template, redirect,request
from flask_app import app 
from flask_app.models.dojo_model import Dojos

#-----dojos route / this renders html /-----#
@app.route('/dojos')
def all_dojos (): 
    dojos = Dojos.get_all()

    return render_template('dojos.html',dojos=dojos)

#----- redirects main page to dojos page -----#
@app.route('/')
def redirect_dojos (): 
    return redirect('/dojos')

#----creates dojo with create class method-----# 
@app.route('/create_dojo',methods=['POST'])
def create_dojo():
    Dojos.create(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:uid>')
def view_dojo(uid):
    data = {
        'id' : uid
    }
    # dojo = Dojos.get_one_with_ninjas(data)

    return render_template ('dojo_show.html',dojos=Dojos.get_one_with_ninjas(data))

# @app.route('/dojo')
# def view_dojo():

    
#     return render_template ('dojo_show.html')