class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        maxLen = 1
        ans = s[0]

        for length in range(2,n+1):
            for row in range(n):
                col = row + length - 1
                if col < n:
                    if length == 2:
                        if s[row] == s[col]:
                            dp[row][col] = 1
                            if length > maxLen:
                                maxLen = length
                                ans = s[row:col+1]    
                        else:
                            dp[row][col] = 0
                    else:
                        if s[row] == s[col] and dp[row+1][col-1] == 1:
                            dp[row][col] = 1
                            if length > maxLen:
                                maxLen = length
                                ans = s[row:col+1]
                        else:
                            dp[row][col] = 0
        return ans

