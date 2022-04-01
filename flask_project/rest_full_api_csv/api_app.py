from flask import Flask
from flask_restful import Api, Resource, reqparse

from user import User

app = Flask(__name__)
api = Api(app)

# Add URL endpoints
api.add_resource(User, '/users')

if __name__ == '__main__':
    app.run(debug=True)
