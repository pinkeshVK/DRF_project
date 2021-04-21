import requests
import json

URL = "http://127.0.0.1:8000/api3/"
headers = {'content-Type': 'application/json'}


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    res = requests.get(url=URL, headers=headers, data=json_data)
    data = res.json()
    print(data)


get_data()


def post_data():
    data = {
        'name': 'Amanda',
        'age': 32
    }

    json_data = json.dumps(data)
    res = requests.post(url=URL, headers=headers, data=json_data)
    print(res.json())


post_data()


def update_data():
    data = {
        'id': 1,
        'name': 'Rox',
        # we are providing all fields if we want to update partially remove 1 field and set partially =true
    }
    json_data = json.dumps(data)
    res = requests.put(url=URL, headers=headers, data=json_data)
    print(res.json())


# update_data()


def delete_data():
    data = {'id': 2}
    json_data = json.dumps(data)
    res = requests.delete(url=URL, headers=headers, data=json_data)
    print(res.json())

# delete_data()
