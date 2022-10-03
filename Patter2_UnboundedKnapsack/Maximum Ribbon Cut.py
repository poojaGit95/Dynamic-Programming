'''
given a ribbon of length N
form N using the lengths of segments s {} such that we get max count of segements selected
'''

import math
def maxRibbonSegments(segments, ribbonSize):

    dp = [[0] * (ribbonSize + 1) for i in range(len(segments) + 1)]

    for i in range(ribbonSize + 1):
        dp[0][i] = -math.inf

    for i in range(len(segments) + 1):
        dp[i][0] = 0

    for i in range(1, len(segments) + 1):
        for j in range(1, ribbonSize + 1):

            if j<segments[i - 1]:
                dp[i][j] = dp[i-1][j]
            else:
                if dp[i-1][j- segments[i-1]]!=-math.inf:
                    dp[i][j] = max(dp[i-1][j], 1 + dp[i][j - segments[i - 1]])
                else:
                    dp[i][j] = dp[i - 1][j]
    print(dp)
    return dp[len(segments)][ribbonSize]

result = maxRibbonSegments([1,2,3],17)
print(result)