from urllib.parse import parse_qsl

query = 'name=chenzhiyuan&age=24'
print(parse_qsl(query))
