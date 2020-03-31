# 问题62：一个机器人位于一个m*n网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 问总共有多少条不同的路径？
import numpy as np
m=7
n=3
# 普通动态规划，复杂度m*n
def uniquePaths(m,n):
    dp=np.zeros((m,n),dtype=int)
    dp[:,0]=1
    dp[0,:]=1
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    return dp[m-1][n-1]

print(uniquePaths(m,n))

def optUniquePaths(m,n):
    cur = [1] * n
    for i in range(1,m):
        for j in range(1,n):
            cur[j]+=cur[j-1]
    return cur[n-1]
print(optUniquePaths(m,n))
