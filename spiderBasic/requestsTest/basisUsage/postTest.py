import requests

data = {'name':'chenzhiyuan','age':'24'}
r = requests.post("http://httpbin.org/post", data=data)
print(r.text)
