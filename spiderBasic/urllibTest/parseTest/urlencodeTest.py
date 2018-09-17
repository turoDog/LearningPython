from urllib.parse import urlencode

params = {
    'name': 'chenzhiyuan',
    'age': 24
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)
