import pandas as pd
import requests
from flask_restful import reqparse, Resource, request


class User(Resource):
    def get(self):
        """

        :return:
        """
        data = pd.read_csv('users.csv')
        data = data.to_dict('records')
        return {'data': data}, 200

    def post(self):
        """
        we can use request as well
        :return:
        """
        print("request json data")
        print(request.json)
        print("*"*100)
        # print(request.__dict__)
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('age', required=True)
        parser.add_argument('city', required=True)
        args = parser.parse_args()

        data = pd.read_csv('users.csv')
        new_data = pd.DataFrame({
            'name': [args['name']],
            'age': [args['age']],
            'city': [args['city']]
        })

        # unique_name = data['name'].unique()
        # all_name = data['name'].tolist()
        # print(f"unique_name: {unique_name}")
        # print(f"all_name: {all_name}")
        is_name_exist = (data['name'] == args['name']).any()
        print(f"is_name_exist:::: {is_name_exist}")
        if is_name_exist:
            message = "Name is already in the dataset!!"
            print(message)
            new_data["message"] = message
            return {'data': new_data.to_dict('records')}, 400
        else:
            data = data.append(new_data, ignore_index=True)
            data.to_csv('users'
                        '.csv', index=False)
            return {'data': new_data.to_dict('records')}, 201

    def delete(self):
        """

        :return:
        """
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        args = parser.parse_args()

        data = pd.read_csv('users.csv')

        data = data[data['name'] != args['name']]

        data.to_csv('users.csv', index=False)
        return {'message': 'Record deleted successfully.'}, 200

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('age', required=True)
        parser.add_argument('city', required=True)
        args = parser.parse_args()

        data = pd.read_csv('users.csv')

        new_data = pd.DataFrame({
            'name': [args['name']],
            'age': [args['age']],
            'city': [args['city']]
        })
        if new_data['name'] == data['name']:
            data = data.append(new_data, ignore_index=True)
        else:
            print(f"Nothing to update!!")
            data = data
        data.to_csv('users'
                    '.csv', index=False)
        return {'data': new_data.to_dict('records')}, 201
