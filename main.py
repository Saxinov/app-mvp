from flask import Flask

app = Flask(__name__)

@app.route('/')
def greet():
    return "<h1>Hello Alex</h1>"