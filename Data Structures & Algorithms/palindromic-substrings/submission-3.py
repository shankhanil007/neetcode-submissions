class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        count = n

        for length in range(2,n+1):
            for row in range(n):
                col = row + length - 1
                if col < n:
                    if s[row] == s[col] and ((length == 2) or dp[row+1][col-1] == True):
                        dp[row][col] = True
                        count += 1
                    
        return count
