from urllib.parse import parse_qs

query = 'name=chenzhiyuan&age=24'
print(parse_qs(query))
