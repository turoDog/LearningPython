import requests

r = requests.get("https://www.taobao.com", timeout = 10)
print(r.status_code)
