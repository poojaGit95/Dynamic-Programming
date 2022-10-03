'''
Target sum - leetcode 494
Add + or - between nums to get target sum
this problem can be solved as 2 subsets with diff equal to target
s1 - s2 = target
s1 + s2 = sum
s1 + (sum-s1) = target
s1 = (target - sum) // 2
now count number of ways to get  target for s1
'''


def targetSum(nums, finalTarget):

    sumVal = sum(nums)
    target = (finalTarget+sumVal)//2

    n = len(nums)
    dp = [[0] * (target + 1) for i in range(n + 1)]

    for i in range(target+1):
        dp[0][i] = 0

    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, target+1):

            if j<nums[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
    return dp[n][target]

result = targetSum([1,1,1,1,1], 1)
print(result)