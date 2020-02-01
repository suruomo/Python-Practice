import random
# 猜0~100之间的数字
number=random.randint(0,100)
while True:
    p=int(input("请输入0-100之间的数字："))
    if p>number:
        print("猜大了")
    elif p<number:
        print("猜小了")
    else:
        print("猜对啦！")
        break

