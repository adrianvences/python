from flask import Flask

app = Flask (__name__)

@app.route('/')
def hello_world ():
    return "hello world"

@app.route('/dojo')
def dojo ():
    return "dojo"

@app.route('/hi/<name>')
def hi (name):
    print(name)
    return "Hi, " + name 

@app.route ('/repeat/<int:num1>/<word>')
def repeat(num1,word):
    return word * num1

if __name__ == "__main__":
    app.run(debug= True)