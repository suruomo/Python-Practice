import requests
url="https://www.amazon.cn/dp/B00AJJJNLE/ref=lp_754386051_1_2?s=music&ie=UTF8&qid=1583826256&sr=1-2"
r=requests.get(url)
r.encoding=r.apparent_encoding
# python请求返回503
print(r.status_code)
print(r.request.headers)
# 修改user-agent
kv={'user-agent':'Mozilla/5.0'}
r=requests.get(url,headers=kv)
print(r.status_code)
print(r.text[1000:2000])