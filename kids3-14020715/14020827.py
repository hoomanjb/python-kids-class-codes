# REST - RESTFULL - API - web services

# REST = representational state transfer
# API = application programming interface

# Http

# GET - POST - PUT - PATCH - DELETE
# fname lname phone
# https://api.github.com/users/<username>

# Status code
# 201-200 ok - successful
# 3** Redirection
# 4** - 404, 403 - Client Error
# 5** - 503  Server Error


# #########################################
# requests urlib3 curl
import requests
import json

# api_url = "https://jsonplaceholder.typicode.com/todos"
# response = requests.get(api_url)
# if response.status_code == 200:
#     print('ok')
#
# a = response.json()
# print(response.headers)
# print(a)
# for item in a:
#     print(item)
# print(type(a))



# api_url = "https://jsonplaceholder.typicode.com/todos"
# todo = {'userId': 1, "title": 'Test', "completed": False}
#
# response = requests.post(api_url, json=todo)
# if response.status_code == 200:
#     print('ok')

# api_url = "https://jsonplaceholder.typicode.com/todos/1"
# response = requests.get(api_url)
# if response.status_code == 200:
#     print('ok')


# api_url = "https://jsonplaceholder.typicode.com/todos"
# todo = {'userId': 1, "title": 'Test', "completed": False}
# headers = {'Content-Type': 'application/json', 'Token': 'logintoken'}
# response = requests.post(api_url, data=json.dumps(todo), headers=headers)
# if response.status_code == 200:
#     print('ok')

# #######################################

# get /transactions  get all items\
# get /events/<event_id>/guests    /events/5/guests
# get /events/<event_id>/guests/<guest_id>
# get /transactions/<id>  get item 5

# post 	/events/<event_id>/guests
# post /transactions  send data for create

# put /transactions/<id>
# patch /transactions/<id>
# delete /transactions/<id>

# #########################################

# django-rest-framework
# fast-api


