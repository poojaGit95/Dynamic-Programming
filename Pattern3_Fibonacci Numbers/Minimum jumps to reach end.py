'''
given an array of nums, move to end with minimum no. of jumps
'''
import math
def minJumps(jumps):
    dp = [math.inf]*(len(jumps))
    dp[0] = 0
    pos = [-1]*(len(jumps))
    pos[0] = 0
    for i in range(1, len(jumps)):
        for j in range(0, i):

            if j+jumps[j]>=i:
                if dp[i]>1+dp[j]:
                    dp[i] = min(dp[i], 1+dp[j])
                    pos[i] = j
    print(dp)
    print(pos)
    return dp[-1]

result = minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9])
print(result)

