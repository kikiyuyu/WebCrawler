import requests
from bs4 import BeautifulSoup
import lxml
import re

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4)\
        AppleWebKit/537.36(KHTML, like Gecko) Chrome/52 .0.2743. 116 Safari/537.36'

    }  # 模拟浏览器访问
    response = requests.get(url, headers=headers)  # 请求访问网站
    html = response.text  # 获取网页源码
    return html  # 返回网页源码

c_url="https://gamepedia.jp/ac-switch/archives/6987"
soup = BeautifulSoup(get_html(c_url), 'lxml')

page_list = []
for div in soup.find_all(name="div"):
    classname = div.get("class")
    if classname:
        if classname[0] == "table-sort":
            for a in div.find_all(name="a"):
                a_classname = a.get("class")
                if a_classname:
                    continue

                page_list.append(int(re.findall(r'\d+',a.get("href"))[0]))

print(page_list)