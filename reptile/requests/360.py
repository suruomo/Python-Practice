import requests
kv={'q':'Python'}
r=requests.get("http://www.so.com",params=kv)
print(r.status_code)
print(r.request.url)