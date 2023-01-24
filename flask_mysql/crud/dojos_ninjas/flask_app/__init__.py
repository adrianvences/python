from flask import Flask
app = Flask(__name__)
app.secret_key = "rootroot"

DATABASE = "dojos_and_ninjas_schema"