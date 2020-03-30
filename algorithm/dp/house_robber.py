import numpy

# 一堆数字选最大一组，且该组数字不相邻
data = [1, 2, 4, 1, 7, 8, 3]


# 递归求解
def rec_opt(data, i):
    if i == 0:
        return data[0]
    elif i == 1:
        return max(data[0], data[1])
    else:
        # 选择当前数字
        A = rec_opt(data, i - 2) + data[i]
        # 不选当前数字
        B = rec_opt(data, i - 1)
        return max(A, B)


print("递归解法：",rec_opt(data,6))

# 非递归求解:动态规划
def dp_opt(data):
    dp = numpy.zeros(len(data))
    dp[0] = data[0]
    dp[1] = data[1]
    for i in range(2, len(data)):
        dp[i] = max(dp[i - 2] + data[i], dp[i - 1])
    return dp[len(data)-1]

print("动态规划结果：", dp_opt(data))
