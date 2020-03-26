from bs4 import BeautifulSoup
import requests
import time
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}


def get_info(url, file):
    res = requests.get(url, headers=headers)
    res.encoding = file.encoding  # 同样读取和写入的编码格式
    soup = BeautifulSoup(res.text, 'lxml')
    ranks = soup.select('span.pc_temp_num')
    titles = soup.select('a.pc_temp_songname')
    times = soup.select('span.pc_temp_time')
    for rank, title, time in zip(ranks, titles, times):
        data = {
            'rank': rank.get_text().strip(),
            'title': title.get_text().strip(),
            'time': time.get_text().strip()
        }
        string = "{: <10}{: <30}{: <10}\n".format(data['rank'], data['title'], data['time'])  # 格式化输出
        file.write(string)


def get_website_encoding(url):  # 一般每个网站自己的网页编码都是一致的,所以只需要搜索一次主页确定
    res = requests.get(url, headers=headers)
    charset = re.search("charset=(.*?)>", res.text)
    if charset is not None:
        blocked = ['\'', ' ', '\"', '/']
        filter = [c for c in charset.group(1) if c not in blocked]
        return ''.join(filter)  # 修改res编码格式为源网页的格式,防止出现乱码
    else:
        return res.encoding  # 没有找到编码格式,返回res的默认编码


if __name__ == '__main__':
    encoding = get_website_encoding('http://www.kugou.com')
    urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(str(i)) for i in range(1, 23)]
with open(r'F:\Python code\爬虫案例/kugou_500.txt', 'w', encoding=encoding) as f:
    f.write("排名      歌手         歌名          长度\n")
    for url in urls:
        get_info(url, f)
        time.sleep(1)  # 缓冲一秒,防止请求频率过快
