import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'
                 '537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
r = requests.get("https://www.zhihu.com/explore",headers=headers)
print(r.text)
