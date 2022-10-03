'''
solve this to find the longest palindrome subsequence. Now find the diff of actual string with
the computed palindrome subsequence
'''

def minDeletions(s):

    n = len(s)

    dp = [[0]*n for i in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for l in range(2, n+1):
        for i in range(0, n-l+1):
            j = i+l-1
            if l==2 and s[i]==s[j]:
                dp[i][j] = 2
            elif s[i]==s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
    palindrom_len = dp[0][n-1]
    min_deletions = n-palindrom_len
    return min_deletions

#result = minDeletions("agbdba")
result = minDeletions("BBABCBCAB")
print(result)