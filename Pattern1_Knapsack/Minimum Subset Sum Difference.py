'''
give a set of nums, find to 2 subsets such that subsets have low sum has lowest difference.
same as subset sum problem, here take target as sum(nums)//2
Take Last true from the last row
'''

def minDiffSubset(nums):

    n= len(nums)
    sumVal = sum(nums)

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

    for i in range(target,-1,-1):
        if dp[n][i] == 1:
            return i


result = minDiffSubset([1,5,11,5])
print(result)
diff = abs(result - (sum([1,6,11,5]) - sum([1,6,11,5])//2))
print(diff)