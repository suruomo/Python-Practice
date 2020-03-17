from bs4 import BeautifulSoup
import requests
import re

kv={'user-agent':'Mozilla/5.0'}
url="http://python123.io/ws/demo.html"
r=requests.get(url,headers=kv)
demo=r.text
soup=BeautifulSoup(demo,"html.parser")

# print(soup.find_all(['a','b']))

for tag in soup.find_all(True):
    print(tag.name)
for tag in soup.find_all(re.compile('b')):
    print(tag.name)