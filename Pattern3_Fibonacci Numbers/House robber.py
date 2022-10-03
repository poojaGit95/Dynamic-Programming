'''
House robber - leetcode
'''

def houseRobber(house):

    dp = [0]*len(house)

    dp[0] = house[0]
    dp[1] = max(house[1], dp[0])

    for i in range(2, len(house)):
        dp[i] = max(dp[i-2]+house[i], dp[i-1])
    return dp[-1]

result = houseRobber([5, 3, 4, 11, 2])
print(result)