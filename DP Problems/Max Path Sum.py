'''
Find max possible sum for a path from top left to bottom right
dp[m][n] = max(dp[m-1][n], dp[m][n-1]) + arr[m][n]
'''
import math
def maxSum(arr):

    m = len(arr)
    n = len(arr[0])
    dp = [[0]*n for i in range(m)]

    dp[0][0] = arr[0][0]
    for i in range(1, n):
        dp[0][i] = arr[0][i] + dp[0][i-1]

    for i in range(1, m):
        dp[i][0] = arr[i][0] + dp[i-1][0]

    for i in range(1,m):
        for j in range(1, n):
            dp[i][j] = arr[i][j] + max(dp[i-1][j], dp[i][j-1])

    return dp[m-1][n-1]

result = maxSum([[3,7], [9,8]])
print(result)




