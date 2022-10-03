'''
for a given string find the longest palindrome subsequence
required n*n matrix, n is length of string
intially add values for l=1 and l=2
then create a loop for adding values from l=3 to total length
if s[first char]!=s[last char] -> dp[i][j] = max(dp[i][j-1], dp[i+1][j])
else dp[i][j] = 2 + dp[i+1][j-1], i.e. 2 chars (first&last) plus palindrome of remianing string
i.e. the middle part
always result is stored in last index of first row
'''

def palindromeSubsequence(s):

    n = len(s)
    dp = [[0]*n for i in range(n)]

    #for l=1
    for i in range(n):
        dp[i][i]=1

    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i+l-1
            if l==2 and s[i]==s[j]:
                dp[i][j] = 2
            elif s[i]==s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
    return dp[0][n-1]
result = palindromeSubsequence("BBABCBCAB")
print(result)