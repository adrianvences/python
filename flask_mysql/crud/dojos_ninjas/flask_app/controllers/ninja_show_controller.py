from flask import Flask ,render_template

from flask_app import app 
@app.route('/dojo_ninjas')
def Dojo_Ninjas_Page (): 
    return render_template('ninja_show.html')