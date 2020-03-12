import requests
import os
root="F://picture//"
url="http://p9.qhimg.com/bdm/1024_768_85/t01f551f7694e571879.jpg"
path=root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("保存失败")
except:
    print("爬取失败")
