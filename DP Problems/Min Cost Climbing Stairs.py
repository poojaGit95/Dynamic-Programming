'''
Calculate min cost to reach Nth stair by taking 1 or steps
'''

def minCost(arr):

    dp = [0]*len(arr)

    # 1st step
    dp[0] = arr[0]

    #2nd step
    dp[1] = min(arr[0], arr[1])

    for i in range(2, len(arr)):
        dp[i] = min(dp[i-1], dp[i-2]) + arr[i]

    return dp[-1]

result = minCost([3,2,4,5])
print(result)
