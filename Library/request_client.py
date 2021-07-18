from django.http import response
import requests 

GET_SINGLE_DATA_URL="http://127.0.0.1:8000/get-stud/"

def get_single_data(id):
    response = requests.get(GET_SINGLE_DATA_URL + str(id) + '/')
    print(response.json())

# get_single_data(1)

GET_ALL_DATA_URL="http://127.0.0.1:8000/get-all-stud/"
def get_all_data():
    response = requests.get(GET_ALL_DATA_URL)
    print(response.json())

# get_all_data()

# API_URL = "http://127.0.0.1:8000/student-api/"
CLASS_API_URL = "http://127.0.0.1:8000/stud-class-api/"    
import json
def get_single_or_alldata(sid=None):
    data = {}
    if sid:
        data = {"id": sid}
    # data = {"id": 1}
    json_data = json.dumps(data)
    resp = requests.get(CLASS_API_URL,data=json_data)
    print(resp.json())

# get_single_or_alldata(5)

def post_data(d):
    # json_data=json.dumps(d)
    reps=requests.post(CLASS_API_URL,json=d)
    print(reps.json())

# d = {"name":"Ravi","age":19,"city":"Pune","marks":75}
# post_data(d)

def put_data(data):
    # json_data = json.dumps(data)
    requests.put(CLASS_API_URL,json=data)
    print(response.json)


# d = {"id":5,"name":"ABCD","city":"Alibaug","marks":74}
# d = {"id":4, "name": "EEE"}
# put_data(d)

def delete_data(dat):
    resp = requests.delete(CLASS_API_URL, json=dat)
    print(resp.json())

# delete_data({'id': 4})
#############################################################
API_URL = "http://127.0.0.1:8000/studentapi/"
import json
headers = {'Content-Type': 'application/json'}
def get_single_or_alldata(sid=None):
    data = {}
    if sid:
        data = {"id": sid}
    # data = {"id": 1}
    json_data = json.dumps(data)
    resp = requests.get(API_URL,headers = headers, data=json_data)
    print(resp.json())

# get_single_or_alldata(5)

def post_data(d):
    # json_data=json.dumps(d)
    reps=requests.post(API_URL,headers = headers,json=d)
    print(reps.json())

d = {"name":"Ravi","age":23,"city":"Pune","marks":75}
# post_data(d)

def put_data(data):
    # json_data = json.dumps(data)
    requests.put(API_URL,headers = headers,json=data)
    print(response.json)


# d = {"id":14,"name":"ABCD","city":"Alibaug","marks":74}
# d = {"id":12, "name": "EEE"}
# put_data(d)

def delete_data(dat):
    resp = requests.delete(API_URL,headers = headers, json=dat)
    print(resp.json())

# delete_data({'id': 1})