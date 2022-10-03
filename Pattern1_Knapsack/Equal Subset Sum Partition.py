'''
give a set of nums, find to 2 subsets of equal sum possible.
same as subset sum problem, here take target as sum(nums)//2
If sum is odd return false else perform subset sum on target
'''

def equalSubsetPossible(nums):

    n= len(nums)
    sumVal = sum(nums)

    if sumVal%2==1:
        return False

    target = sumVal//2

    dp = [[0]*(target+1) for i in range(n+1)]

    for i in range(target+1):
        dp[0][i] = 0

    for i in range(n+1):
        dp[i][0] = 1



    for i in range(1, n+1):
        for j in range(1, target+1):

            if j<nums[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
    return dp[n][target]==1

result = equalSubsetPossible([1,5,11,5])
print(result)