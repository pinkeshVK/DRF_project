import requests
import json
get_url_all = "http://127.0.0.1:8000/app2/all/"

def get_url_id(id):
    url_for_id = f"http://127.0.0.1:8000/app2/{id}"
    return url_for_id

post_url="http://127.0.0.1:8000/app2/post/"

req = requests.get(get_url_all)
resp = req.json()
print(resp)

id1 = input("enter id of student >0 and <3 : ")
print(get_url_id(id1))
req2 = requests.get(get_url_id(id1))
resp2 = req2.json()
print(resp2)

#POST

data = {
    'name' : 'Post data',
    'age' : 27
}
json_data = json.dumps(data)
print(json_data)
req_post = requests.post(url=post_url,data= json_data)
resp3 = req_post.json()
print(resp3)