from bs4 import BeautifulSoup
import requests

kv={'user-agent':'Mozilla/5.0'}
url="http://python123.io/ws/demo.html"
r=requests.get(url,headers=kv)
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
print(soup.title)
# 获取a标签名字
print(soup.a.name)
print(soup.a.string)
# 获取a标签父母标签的名字
print(soup.a.parent.name)
tag=soup.a
print(tag.attrs)
print(tag.attrs['class'])
# 查看类型
print(type(tag.attrs))
# 处理有注释内容
newsoup=BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>","html.parser")
print(newsoup.b.string)
print(type(newsoup.b.string))
print(newsoup.p.string)
print(type(newsoup.p.string))
