'''nCr - select r items from n given items
if n==r: -> 1
if n<r -> 0
else
dp[n][r] = (dp[n-1][r-1] + dp[n-1][[r])
'''

def combinationsPossible(n, r):
    dp = [[0]*(r+1) for i in range(n+1)]

    for i in range(r+1):
        dp[0][i] = 0

    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, r+1):

            if i==j:
                dp[i][j]=1
            elif j>i:
                continue
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    return dp[n][r]

result = combinationsPossible(5,4)
print(result)

