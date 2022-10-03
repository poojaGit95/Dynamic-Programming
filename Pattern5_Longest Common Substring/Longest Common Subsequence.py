'''
Find longest common substring for 2 strings s1 and s2
intialise dp[len(s1)+1][[len(s2)+1] and dp[i][0]=0, dp[0][i]=0,
dp[i][j] = 1 + dp[i-1][j-1] when s1[i]==s2[j]
dp[i][j] = max(dp[i-1][j], dp[i][j-1]) when s1[i!=s2[j]
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
    return dp[m][n]

#result = longestCommonSubsequence("abc", "ahjbckl")

result = longestCommonSubsequence("heap", "pea")
print(result)
