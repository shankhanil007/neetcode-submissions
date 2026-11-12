class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        l1 = len(word1)
        l2 = len(word2)

        # memo = {}

        # def helper(i , j):

        #     # Base cases
        #     if i == l1:
        #         return l2 - j  # Insert remaining characters of word2
        #     if j == l2:
        #         return l1 - i  # Delete remaining characters of word1
            
        #     state = (i, j)
        #     if state in memo:
        #         return memo[state]

        #     if word1[i] == word2[j]:
        #         memo[state] = helper(i+1, j+1)
        #         return memo[state]

        #     insert = helper(i, j+1)
        #     delete = helper(i+1, j)
        #     replace = helper(i+1, j+1)

        #     memo[state] = 1 + min(insert, delete, replace)
        #     return memo[state]

        # return helper(0, 0)

        dp = [[float("inf")] * (l2+1) for _ in range(l1+1)] ## Default value is not 0 but float("inf")

        for j in range(l2+1):
            dp[l1][j] = l2 - j
        for i in range(l1+1):
            dp[i][l2] = l1 - i
        
        for i in range(l1-1, -1, -1):
            for j in range(l2-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    insert = dp[i][j+1] 
                    delete = dp[i+1][j] 
                    replace = dp[i+1][j+1]

                    dp[i][j] = 1 + min(insert, delete, replace)
        
        return dp[0][0]



















