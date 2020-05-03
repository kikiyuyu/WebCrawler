import codecs
import json
import lxml
import requests
import re
from bs4 import BeautifulSoup
import pandas as pd


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4)\
        AppleWebKit/537.36(KHTML, like Gecko) Chrome/52 .0.2743. 116 Safari/537.36'

    }  # 模拟浏览器访问
    response = requests.get(url, headers=headers)  # 请求访问网站
    html = response.text  # 获取网页源码
    return html  # 返回网页源码

c_url="https://gamepedia.jp/ac-switch/archives/6987"
soups = BeautifulSoup(get_html(c_url), 'lxml')

page_list = []
for div in soups.find_all(name="div"):
    classname = div.get("class")
    if classname:
        if classname[0] == "table-sort":
            for a in div.find_all(name="a"):
                a_classname = a.get("class")
                if a_classname:
                    continue

                page_list.append(int(re.findall(r'\d+',a.get("href"))[0]))
page_ids = page_list
# page_ids = [1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083]
url = "https://gamepedia.jp/ac-switch/characters/%d/"
content_dict = {}

for i in page_ids:
    print("page : %d" % i)
    soup = BeautifulSoup(get_html(url % i), 'lxml')  # 初始化BeautifulSoup库,并设置解析器
    c_name = soup.find(id="i-2")
    if c_name:
        content_dict[i] = {}
        content_dict[i]['name'] = c_name.string[0:-5]
        for tb in soup.find_all(name='table'):  # 遍历父节点
            for tr in soup.find_all(name='tr'):
                th = tr.find(name="th")
                t_key = th.string
                td = tr.find(name="td")
                if td.string:
                    t_value = td.string
                else:
                    a = td.find(name="a")
                    if a:
                        t_value = a.get_text()
                    else:
                        span = td.find(name="span")
                        if span:
                            t_value = span.string

                content_dict[i][t_key] = t_value
                print("saved page_%d" % i)
print(content_dict)


pd.DataFrame(content_dict).to_csv('shop_pay_count_demo.csv')

# j = json.dumps(content_dict,sort_keys=True, indent=4, separators=(',', ': '))
# file_name = 'json_files/%s.json' % "islander"
# with codecs.open(file_name,"w","utf-8") as f:
#     f.write("var %s =  " % "islander" )
#     f.write(j)