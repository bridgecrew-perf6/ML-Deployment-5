import json.dumps
import requests

url = 'http://127.0.0:8000/model'



request_data = json.dumps({'model': 'knn'})
response = requests.post(url,request_data)

print(response.text)


response.close()