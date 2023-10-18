import requests

# res = requests.get('http://127.0.0.1:5002/')

for i in range(10):
    res = requests.get('http://127.0.0.1:5002/')
    print(res.text)
# print(res.text)