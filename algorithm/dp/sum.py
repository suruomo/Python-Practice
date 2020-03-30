import numpy as np

# 从一堆数字里面选出几个数字的和为给定值，如果存在这样的方案返回true，否则为false
arr = [3, 34, 4, 12, 5, 2]
S = 9


# 递归求解
def rec_sum(arr, i, S):
    # 中途已经找到方案
    if S == 0:
        return True
    # 数组找到最后一个数时还没找到方案
    elif i == 0:
        return arr[0] == S
    # S，不选
    elif arr[i] > S:
        return rec_sum(arr, i - 1, S)
    else:
        # 选择第i个数字
        A = rec_sum(arr, i - 1, S - arr[i])
        # 不选
        B = rec_sum(arr, i - 1, S)
        return A or B


print(rec_sum(arr, len(arr) - 1, S))


# 非递归求解：动态规划
def dp_subset(arr, S):
    # 创建二维数组存储布尔值，len(arr)行，s+1列
    subset = np.zeros((len(arr), S + 1), dtype=bool)
    # 初始化
    # 每行第一个为True
    subset[:, 0] = True
    # 每列第一个为False
    subset[0, :] = False
    # arr[0]==s时为True
    subset[0, arr[0]] = True
    for i in range(1, len(arr)):
        for s in range(i, S + 1):
            if arr[i] > s:
                # 不选
                subset[i, s] = subset[i - 1, s]
            else:
                # 选
                A = subset[i - 1, s - arr[i]]
                # 不选
                B = subset[i - 1, s]
                subset[i, s] = A or B
    # 返回行数，列数
    r, c = subset.shape
    return subset[r - 1, c - 1]


print(dp_subset(arr, 9))
