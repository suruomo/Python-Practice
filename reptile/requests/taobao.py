import requests
import re
def getHTMLText():
    try:
        kv={'user-agent':'Mozilla/5.0'}
        r=requests.get(url,headers=kv,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "获取错误"
def parsePage(list,html):
    try:
        plt=re.findall(r'"view_price":"[\d.]*"',html)
        tlt=re.findall(r'"raw_title":".*?"',html)
        for i in range(plt):
            price=eval(plt[i].split(':')[1])
            title=eval(tlt[i].split(':')[1])
            list.append([price,title])
    except:
        print("解析错误")
def printGoodsList(list):
    print(list)

if __name__=="__main__":
    goods="书包"
    depth=2
    start_url="https://s.taobao.com/search?q="+goods+"&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306"
    infoList=[]
    for i in range(depth):
        try:
            url=start_url+'&s='+str(44*i)
            html=getHTMLText(url)
            parsePage(infoList,html)
            printGoodsList(infoList)
        except:
            print("错误")

