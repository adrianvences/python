from flask import Flask, render_template, session, redirect,request

app = Flask (__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def hello_world ():
    return "hello world"



if __name__ == "__main__":
    app.run(debug= True)