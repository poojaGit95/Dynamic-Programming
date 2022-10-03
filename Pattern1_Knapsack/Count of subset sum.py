'''
Given a set of nums and target, find how many subsets can form target sum.
nums = numbers given
if 0 items and T>0 exists then -> 0
if 0 T and nums  exist then -> 1 (bcoz empty set is subset of nums)
if num>T then -> dp[i-1][j]
if num>T then -> (dp[i-1][j] + dp[i-1][j-nums[i]])
'''

def targetPossible(nums, target):

    n= len(nums)
    dp = [[0]*(target+1) for i in range(n+1)]

    for i in range(target + 1):
        dp[0][i] = 0

    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, target+1):

            if j<nums[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
    print(dp)
    return dp[n][target]

result = targetPossible([2,3,5,6,8,10], 10)
#result = targetPossible([2,3,7,1,4,5], 7)
print(result)