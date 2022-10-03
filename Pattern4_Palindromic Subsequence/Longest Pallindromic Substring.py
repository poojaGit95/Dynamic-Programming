'''
find the longest palindrome substring
keep max count for max length.
dp[i][j] is 1 or 0 based on condition if first and last string in iteration are equal
initialise the dp matrix with 1 for i==j
'''

def longestPalindromeSubstring(s):

    n = len(s)

    dp = [[0]*n for i in range(n)]

    for i in range(n):
        dp[i][i] = 1

    maxLen = 1
    result = ''

    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i+l-1
            if s[i]==s[j]:
                dp[i][j] = 1
                maxLen+=1
                result = result+s[i]
            else:
                dp[i][j] = 0
    print(result)
    print(maxLen)


result = longestPalindromeSubstring("agbdgdba")