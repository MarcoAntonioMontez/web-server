from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>New Heroku App deployed!!</h1>'