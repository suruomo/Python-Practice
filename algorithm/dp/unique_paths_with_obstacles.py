# 问题63,网格中包含障碍
import numpy as np

data=[
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
def uniquePathsWithsObstacles(data):
    if data[0][0]==1:
        return 0
    data[0][0]=1
    for i in range(1,len(data)):
        data[i][0]=1 if (data[i][0]==0 and data[i-1][0]==1) else 0
    for j in range(1,len(data[0])):
        data[0][j]=1 if (data[0][j]==0 and data[0][j-1]==1) else 0
    for i in range(1,len(data)):
        for j in range(1,len(data[0])):
            if data[i][j] !=1:
                data[i][j]=data[i-1][j]+data[i][j-1]
            else:
                data[i][j]=0
    return data[2][2]
print(uniquePathsWithsObstacles(data))