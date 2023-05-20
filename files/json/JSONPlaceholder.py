# example with
# https://jsonplaceholder.typicode.com/
response = requests.get("https://jsonplaceholder.typicode.com/users/1/todos")
todos = json.loads(response.text)
