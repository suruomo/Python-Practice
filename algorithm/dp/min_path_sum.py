# 最小路径和
data = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
def minPathSum(data):
    R = len(data)
    C = len(data[0])
    data[0][0] = 1
    for i in range(R):
        for j in range(C):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                data[i][j] += data[i][j - 1]
            elif j == 0:
                data[i][j] += data[i - 1][j]
            else:
                data[i][j] += min(data[i - 1][j], data[i][j - 1])
    return data[R - 1][C - 1]


print(minPathSum(data))
