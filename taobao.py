import requests
import urllib
import re
import random
from time import sleep


def main():
    url = 'https://s.taobao.com/search?q=%E9%9E%8B&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180112&ie=utf8'
    headers = {"Host": "s.taobao.com",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
               "Accept-Encoding": "gzip, deflate",
               "Content-Type": "text/html;charset=utf-8",
               "referer": "https://s.taobao.com/search?q=%E9%9E%8B&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180111&ie=utf8",
               "cookie": "miid=483738189595270851; l=AoGB-axE4rzHllB2tEc0Jo7AEceaSvWB; thw=cn; cna=4boxEFrKWgECAd9H0CaT6kXH; hng=CN%7Czh-CN%7CCNY%7C156; tracknick=zhouyan1831; t=dc71dff9824a85b012fc309db068c29e; _cc_=WqG3DMC9EA%3D%3D; tg=0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; v=0; cookie2=17ded643dffffa7b2a67954d612d1fec; _tb_token_=77eeeb0476383; uc1=cookie14=UoTdfk1uHc1M3A%3D%3D; enc=5FAGPJC73qqulinvJxI8GW9%2Fi4ZzwyzaiYtMasIsLql3L0TKEEde%2B6nZ9XcPfeQQL6V5ENr3oxLuGcPmK4UWAQ%3D%3D; JSESSIONID=BFF767B268C5C34F8345530DA7B7A7F4; isg=AgMDdlJkXTLMqBxdinZ_WV6WkseteJe6CJ48LzXgWWLZ9CIWvEubCqAmGrNA",
               "Connection": "Keep-Alive"}
    i = 0
    data = {'q': '%E9%9E%8B', 'spm': 'a219r.lm874.1000187.2'}
    content = requests.get(url, headers=headers, data=data, timeout=10).text
    p1 = '//g-search.+?.[jp][pn]g'
    pat = re.compile(p1)
    temp_imgs = pat.findall(content)  # 筛出jpg/png图片信息
    key = []
    for i in range(0, len(temp_imgs), 1):
        key.append(i)
        imgs = dict(zip(key, temp_imgs))
       # print(imgs[i])
        url = 'https:' + str(imgs[i])
        print('https:' + str(imgs[i]))
     #设计字典，并取出图片url
        path = 'D:\\mydata\\jpg\\' + str(i) + '.jpg'
        # 声明存储地址及图片名称
        urllib.request.urlretrieve(url, path)
            # 下载图片
        print(u'下载了第' + str(i+1) + u'张图片')
        #i += 1
        sleep(random.uniform(0.5, 1))
        # 睡眠函数用于防止爬取过快被封IP


if __name__ == '__main__':
    main()
