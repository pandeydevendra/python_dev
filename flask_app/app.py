from flask import Flask, request
import requests
from src.price_prediction import price_by_area #, predict_home_price

app = Flask(__name__)

# way1:
"""
@app.route("/")
def hello():
    return "Hello, World!"
"""


@app.route("/home_price_by_area/<area>")
def home_price_by_area(area):
    print(requests.__dict__)
    price = price_by_area(area)
    return f"Price of home with area {area} is {price}!"


@app.route("/home_price_predict", methods=['GET'])
def home_price_predict():
    print(request.args)
    input_area = request.args.get("area", None)
    input_bed = request.args.get("bed", None)
    input_age = request.args.get("age", None)
    # predict_home_price(input_area, input_bed, input_age)
    return "ok"


# way2:
@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello {name}!"


# o/p: Not Found : if url> http://127.0.0.1:5000/
'''The requested URL was not found on the server. 
If you entered the URL manually please check your spelling and try again.'''
# change url>> http://127.0.0.1:5000/hello/user_name
# Hello user_name!
# eg: http://127.0.0.1:5000/hello/dev
# Hello dev!

if __name__ == '__main__':
    app.run(debug=True)
