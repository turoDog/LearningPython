import json

import requests
from requests.exceptions import RequestException
# 多线程线程池
from multiprocessing.pool import Pool
import re


def get_one_page(url):
    # headers, 伪装成浏览器
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                    'AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/68.0.3440.106 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>'
                        + '.*?data-src="(.*?)"'
                        + '.*?name"><a.*?>(.*?)</a>'
                        + '.*?star">(.*?)</p>'
                        + '.*?releasetime">(.*?)</p>'
                        + '.*?integer">(.*?)</i>'
                        + '.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)

    for item in items:
        yield {
            '排名': item[0],
            '海报': item[1],
            '电影': item[2],
            '主演': item[3].strip()[3:],
            '时间': item[4].strip()[5:],
            '评分': item[5]+item[6]
        }


def write_to_file(content):
    with open('top100.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.flush()
    f.close()


def main(offset):
    url = "http://maoyan.com/board/4?offset=" + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(i*10)
    #pool = Pool()
    #pool.map(main, [i*10 for i in range(10)])
