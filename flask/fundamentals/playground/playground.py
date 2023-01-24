# pair programming with dominic basa

from flask import Flask, render_template

app = Flask (__name__)

@app.route('/play')
def playground():
    return render_template("playground.html", color= 'cyan',times=3)

@app.route('/play/<int:num>')
def displayBoxes(num):
    return render_template("playground.html",color= 'cyan', times=num)

@app.route('/play/<int:num>/<color>')
def displayBoxesColor(num,color):
    
    return render_template ("playground.html", color=color, times=num)
# @app.route('/')

if __name__ == "__main__":
    app.run(debug=True)