from bs4 import BeautifulSoup
import requests

kv={'user-agent':'Mozilla/5.0'}
url="http://python123.io/ws/demo.html"
r=requests.get(url,headers=kv)
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
print(soup.head)
# 下行遍历
# 获取head儿子结点放入列表
print(soup.head.contents)
print(soup.body.contents[1])
# 遍历获取body儿子结点
for child in soup.body.children:
    print(child)
# 遍历获取body子孙结点
for child in soup.body.descendants:
    print(child)
# 上行遍历
# 父亲标签
print(soup.title.parent)
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
# 平行遍历：同一个父亲结点下
print(soup.a.next_sibling)
print(soup.a.next_sibling.next_sibling)
print(soup.a.previous_sibling)
for sibling in soup.a.next_siblings:
    print(sibling)
for sibling in soup.a.previous_siblings:
    print(sibling)