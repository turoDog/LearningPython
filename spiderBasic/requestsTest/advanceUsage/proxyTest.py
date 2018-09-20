import requests

proxies = {
    "http": "http://user:password@10.10.1:3128/"
}
requests.get("https://www.taobao.com", proxies=proxies)
