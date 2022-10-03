'''
W is the weight to be formed
wt = weights given
v = value corresponding the wts.
get max value to form W
if 0 items and W exists then -> 0
if 0 w and wt items exist then -> 0
if wt>W then -> dp[i-1][j]
if wt>W then -> max(dp[i-1][j], val[i]+dp[i][j-wt[i]]
this is unbounded knapsack hence there are infinite number of wts
'''

def maxValue(W, wt, val):
    n = len(wt)
    dp = [[0]*(W+1) for i in range(n+1)]

    for i in range(W+1):
        dp[0][i] = 0

    for i in range(n+1):
        dp[i][0] = 0

    for i in range(1, n+1):
        for j in range(1, W+1):

            if wt[i-1]>j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], val[i-1]+dp[i][j-wt[i-1]])

    return dp[n][W]

#result = maxValue(8, [1,3,4,5],  [10, 40, 50, 70])
result = maxValue(100, [1,50],  [1, 30])
print(result)

