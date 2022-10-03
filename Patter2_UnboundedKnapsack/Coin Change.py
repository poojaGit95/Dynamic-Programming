'''
For this problem calculate number of ways to make given target amount using given designated coins

'''

def numberOfWays(coins, target):

    n = len(coins)
    dp = [[0]*(target+1) for i in range(n+1)]

    for i in range(target+1):
        dp[0][i] = 0

    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, target+1):
            if coins[i-1]>j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
    return dp[n][target]

#result = numberOfWays([1,2,3],4 )
result = numberOfWays([2, 5, 3, 6], 10)
print(result)
