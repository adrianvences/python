# co work with chalie and adrian
from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/accept_info', methods=['POST'])
def accept_info():
    print(request.form)
    session['name']= request.form["name"]
    session["location"] = request.form["location"]
    session["Fav_language"] = request.form["Fav_language"]
    session["Comment"] = request.form["Comment"]


    return redirect("/thanks")

@app.route('/thanks')
def thank_info():
    return render_template('info.html')
    

if __name__=="__main__":
    app.run(debug=True)