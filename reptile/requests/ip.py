import requests
url="http://m.ip138.com/iplookup.asp?ip="
try:
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url + '111.18.76.79', headers=kv)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[-500:])
except:
    print("失败")
