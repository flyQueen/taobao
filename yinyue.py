# coding=utf-8

import requests
import urllib
import re
from time import sleep
import random


def yinyue():
    mp3_data = []
    mp3_title = []
    for ii in range(0, 10):
        url_gangqin = "http://www.htqyy.com/genre/musicList/3?pageIndex=" + str(ii) + "&pageSize=20&order=hot"
        html = requests.request('get', url_gangqin)
        mp3_data.extend(re.findall(r'value="(.*?)"', html.text))
        mp3_title.extend(re.findall(r'title="(.*?)" sid=', html.text))
    url = list(map(lambda x: "http://f1.htqyy.com/play6/" + x + "/mp3/1", mp3_data))
    print(url)
    path = list(map(lambda x:"D:\\mydata\\muisc\\" +x + ".mp3",mp3_title))
    for jj in range(0, len(mp3_data), 1):
       # url = "http://f1.htqyy.com/play6/" + mp3_data[jj] + "/mp3/1"
       # path = "D:\\mydata\\muisc\\" + mp3_title[jj] + ".mp3"

        urllib.request.urlretrieve(url[jj], path[jj])
        print('下载了《' + mp3_title[jj] + '》')
        sleep(random.uniform(0.5, 1))
        # 睡眠函数用于防止爬取过快被封IP

if __name__ == '__main__':
    yinyue()
