class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        l1 = len(s)
        l2 = len(p)

        dp = [[False] * (l2+1) for _ in range(l1+1)]

        dp[l1][l2] = True

        # for i in range(l1):
        #     dp[i][l2] = False
        
        for i in range(l1, -1, -1):
            for j in range(l2-1, -1, -1):
                match = i < len(s) and (s[i] == p[j] or p[j] == ".")
                if (j + 1) < len(p) and p[j + 1] == "*":
                    dp[i][j] = dp[i][j+2] or (match and dp[i+1][j])  
                elif match:
                    dp[i][j] = dp[i+1][j+1]
                    
        return dp[0][0]




