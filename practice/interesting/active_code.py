# 使用 Python 如何生成 200 个激活码
import uuid, random, string

# 方法一：使用uuid
# uuid1()——基于时间戳由MAC地址、当前时间戳、随机数生成。可以保证全球范围内的唯一性，但MAC的使用同时带来安全性问题，局域网中可以使用IP来代替MAC。
for i in range(20):
    print(uuid.uuid1())
# 方法二：使用random模块随机生成
chars = string.digits+string.ascii_letters
print(chars)
# random.sample()可以从指定的序列中，随机的截取指定长度的片断，不作原地修改。
s="".join(random.sample(chars,20))
print(s)
