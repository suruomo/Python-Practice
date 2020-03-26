# 中国大学排名
import bs4
from bs4 import BeautifulSoup
import requests

def getHTMLText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""
def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        # 过滤非标签的字符串类型
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            # 查找大学排名，名称，分数
            ulist.append([tds[0].string,tds[1].string,tds[3].string])
    pass
def printUnivList(ulist,num):
    # ^表示居中
    print("{:^10}\t{:^14}\t{:^10}\t".format("排名","学校名称","分数"))
    for i in range(num):
        u=ulist[i]
        print("{:^10}\t{:^14}\t{:^10}\t".format(u[0],u[1],u[2]))

if __name__=="__main__":
    uinfo=[]
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html"
    html=getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,30)
