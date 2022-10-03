'''
Here find the longest subsequence for s1 and s2 strings
deletions = len(s1) - longest subsequence length
insertions = len(s2) - longest subsequence length
'''

def longestCommonSubsequence(s1, s2):
    m = len(s1)
    n = len(s2)

    dp = [[0]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        dp[i][0] = 0

    for i in range(n+1):
        dp[0][i] = 0

    res = ''
    for i in range(1,m+1):
        for j in range(1, n+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                res = res + s1[i-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(res)
    deletion = m - dp[m][n]
    insertion = n - dp[m][n]
    print("deletion", deletion)
    print("insertion", insertion)
    return dp[m][n]

result = longestCommonSubsequence("heap", "pea")
print(result)
