
import requests
import logging
from requests.packages import urllib3

#urllib3.disable_warnings()
logging.captureWarnings(True)
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)
