import requests

r = requests.get('http://httpbin.org/get')
print(r.text)

data = {
    'age':'24',
    'name':'chenzhiyuan'
}
r1 = requests.get("http://httpbin.org/get",params=data)
print(r1.text)

r2 = requests.get("http://httpbin.org/get")
print(type(r2.text))
print(r2.json())
print(type(r2.json()))
