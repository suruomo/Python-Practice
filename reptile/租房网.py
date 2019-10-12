import requests
from bs4 import BeautifulSoup
import time
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2843.400'
}
def get_links(url):     #获取详情页url
    wb_data=requests.get(url,headers=headers)
    soup=BeautifulSoup(wb_data.text,'lxml')
    links=soup.select('#page_list > ul > li > a ')   #url列表
    for link in links:
        href=link.get("href")
        get_info(href)
def get_info(url):   #获取页面信息
    wb_data=requests.get(url,headers=headers)
    soup=BeautifulSoup(wb_data.text,'lxml')
    titles=soup.select(' div.pho_info > h4')
    addresses=soup.select('span.pr5')
    prices=soup.select('#pricePart > div.day_l > span')

    for title,address,price in zip(titles,addresses,prices):
        data={
            'title':title.get_text().strip(),
            'address':address.get_text().strip(),
            'price':price.get_text().strip()
        }
        print(data)
if __name__=='__main__':
    urls=['https://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(number) for number in range(1,5)]
    for single_url in urls:
        get_links(single_url)
        time.sleep(2)
