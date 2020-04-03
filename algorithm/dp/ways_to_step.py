import numpy as np

n = 7


def waysToStep(n):
    dp = np.zeros(n)
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4
    for i in range(3, n):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return int(dp[n - 1])


print(waysToStep(n))
