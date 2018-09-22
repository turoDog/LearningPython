import re

content = 'Hello 1234567 World_This is a Regex Demo'
print(len(content))
result = re.match('^He.*?(\d+).*Demo$',content)
print(result)
print(result.group(1))
print(result.span())
