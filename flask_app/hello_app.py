from flask import Flask
from .home_price_prediction import predict_home_price
app = Flask(__name__)

# way1:
"""
@app.route("/")
def hello():
    return "Hello, World!"

"""

@app.route("/home_price/<area>")
def hello_name(area):
    price = predict_home_price(area)
    return f"Hello {price}!"




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
