# example with
# https://jsonplaceholder.typicode.com/
import json
import requests
response = requests.get("https://jsonplaceholder.typicode.com/users/1/todos")
todos = json.loads(response.text)
