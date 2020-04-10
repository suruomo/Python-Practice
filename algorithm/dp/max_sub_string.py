# 最大连续子数组和
import numpy as py
num=[-2,1,-3,4,-1,2,1,-5,4]
def maxSubArray(num):
    for i in range(len(num)):
        num[i]+=max(num[i-1],0)
    return max(num)
print(maxSubArray(num))