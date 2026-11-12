class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        ## ----------- Approach 1 -----------

        # n = len(s)
        # dp = [[False] * n for _ in range(n)]

        # for i in range(n):
        #     dp[i][i] = True

        # maxLen = 1
        # start = 0

        # for length in range(2,n+1):
        #     for row in range(n):
        #         col = row + length - 1
        #         if col < n:
        #             if s[row] == s[col] and ((length == 2) or dp[row+1][col-1] == True):
        #                 dp[row][col] = True
        #                 if length > maxLen:
        #                     maxLen = length
        #                     start = row
                    
        # return s[start: start+maxLen]

        ## ----------- Approach 2 -----------

        n = len(s)
        maxLen = 1
        ans = s[0]

        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                length = r - l + 1
                if length > maxLen:
                    maxLen = length
                    ans = s[l: r+1]
                l -= 1
                r += 1

            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                length = r - l + 1
                if length > maxLen:
                    maxLen = length
                    ans = s[l: r+1]
                l -= 1
                r += 1
        return ans


