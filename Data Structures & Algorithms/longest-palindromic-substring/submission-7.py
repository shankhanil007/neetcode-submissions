class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        maxLen = 1
        start = 0

        for length in range(2, n+1):
            for row in range(n):
                col = row + length - 1
                if col < n:
                    if s[row] == s[col] and (length==2 or dp[row+1][col-1]):
                        dp[row][col] = True

                        if length > maxLen:
                            maxLen = length
                            start = row
        
        return s[start: start+maxLen]