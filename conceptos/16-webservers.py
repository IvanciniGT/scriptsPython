import requests

api_url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(api_url)
print(response.json())

api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
print(response.json())
print(response.status_code)