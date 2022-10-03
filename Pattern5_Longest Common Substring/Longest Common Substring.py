'''
Find longest common substring for given strings s1 and s2
keep track of max length using a count
'''

def longestCommonSubString(s1, s2):
    m = len(s1)
    n = len(s2)

    dp = [[0]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        dp[i][0] = 0

    for j in range(n+1):
        dp[0][j] = 0

    res = ''
    maxLen = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                if maxLen<dp[i][j]:
                    maxLen = max(maxLen, dp[i][j])
                    res = res + s1[i-1]

    print(res)
    return maxLen

result = longestCommonSubString("abcdghjk", "tyuabcd")
print(result)
