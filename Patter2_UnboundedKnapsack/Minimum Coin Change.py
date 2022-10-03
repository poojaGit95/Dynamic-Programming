'''
given a set of coins, find the min number of coins required to make the target
note each designation of coin is infinitely available
this problem is same as unbounded knapsack
'''

import math
def minCoinChange(coins, target):

    dp = [[0]*(target+1) for i in range(len(coins)+1)]

    for i in range(target+1):
        dp[0][i] = math.inf

    for i in range(len(coins)+1):
        dp[i][0] = 0

    for i in range(1, len(coins)+1):
        for j in range(1, target+1):

            if j<coins[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j], 1+dp[i][j-coins[i-1]])
    return dp[len(coins)][target]

result = minCoinChange([9, 6, 5, 1], 11)
print(result)
