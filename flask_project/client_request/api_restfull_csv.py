from pprintpp import pprint as pp

import requests

url = "http://127.0.0.1:5000/users"


def add_user():
    payload = {'name': 'Sachin2',
               'age': '32',
               'city': 'Pune'}
    files = [

    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)


def get_all_user():
    payload = {'name': 'Sachin',
               'age': '35',
               'city': 'Mumbai'}
    files = [

    ]
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload, files=files)

    pp(response.json())


if __name__ == "__main__":
    # get_all_user()
    add_user()
