import urllib.request

response = urllib.request.urlopen('https://www.python.org')
print(response.read().decode('utf-8'))# 抓取网页并以 utf-8 格式解析
print(type(response))# 打印 response 的类型
print(response.status)# 打印 response 的状态码
print(response.getheaders())# 响应头
print(response.getheader('Server'))# 响应服务器


