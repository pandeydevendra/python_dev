from flask import Flask

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome"


@app.route("/home")
def home():
    return "Welcome to home"


from controller import *


if __name__ == '__main__':
    app.run(debug=True)
