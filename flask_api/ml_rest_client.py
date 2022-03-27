import json
import requests


url = 'http://127.0.0.1:8000/model'
gcp = 'http://34.125.173.20:8005/model'
colab = 'http://acbe-34-86-102-118.ngrok.io/predict'

request_data = json.dumps({'age':40, 'salary':60000})

response = requests.post(colab, request_data)

print (response.text)