from bs4 import BeautifulSoup
import requests

kv={'user-agent':'Mozilla/5.0'}
url="http://python123.io/ws/demo.html"
r=requests.get(url,headers=kv)
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))