'''
Count total ways to reach nth stair by choosing 1 or 2 steps at a time
'''

def climbStair(n):

    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

print(climbStair(4))