'''
L is the length of the rod
length = length of pieces given
prices = prices corresponding the l.
get max value to form L
if 0 items and L exists then -> 0
if 0 L and l items exist then -> 0
if l>L then -> dp[i-1][j]
if l>L then -> max(dp[i-1][j], price[i]+dp[i][j-l[i]]
this is unbounded knapsack hence there are infinite number of wts
'''

def maxValue(L, lengths, prices):
    n = len(lengths)
    dp = [[0]*(L+1) for i in range(n+1)]

    for i in range(L+1):
        dp[0][i] = 0

    for i in range(n+1):
        dp[i][0] = 0

    for i in range(1, n+1):
        for j in range(1, L+1):

            if lengths[i-1]>j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], prices[i-1]+dp[i][j-lengths[i-1]])
    print(dp)
    return dp[n][L]

#result = maxValue(8, [ 1,2,3,4,5,6,7,8],  [ 1,5,8,9,10,17,17,20])
result = maxValue(8, [ 1,2,3,4,5,6,7,8],  [ 3,5,8,9,10,17,17,20])
print(result)

