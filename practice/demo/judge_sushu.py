# 找出1---100之间的所有素数
i = 1
while i <= 100:
    j = 2
    flag = 0
    while j < i:
        if (i % j == 0):
            flag = 1  # 不是素数
            break;
        else:
            j = j + 1
            flag = 0
    if flag == 0:
        print(i, "是素数")
    else:
        print(i, "不是素数")
    i = i + 1
