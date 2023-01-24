from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'iamstealth'

@app.route('/')
def index():
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/dashboard')

@app.route('/thanks')
def thanks():

    if not 'name' in session:
        return redirect('/order')
    if not 'qty' in session:
        return redirect('/order')
    return render_template('thanks_order.html')

@app.route('/order/<product>')
def place_order(product):
    return render_template("form.html",product=product)

@app.route('/accept_order', methods=['POST'])
def accept_order():
    print(request.form)

    session["name"] = request.form['name']
    session["qty"] = request.form['qty']
    session["product"] = request.form['product']

    return redirect('/thanks')


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.