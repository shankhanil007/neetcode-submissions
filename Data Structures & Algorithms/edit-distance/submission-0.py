class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        l1 = len(word1)
        l2 = len(word2)

        memo = {}

        def helper(i , j):

            # Base cases
            if i == l1:
                return l2 - j  # Insert remaining characters of word2
            if j == l2:
                return l1 - i  # Delete remaining characters of word1
            
            state = (i, j)
            if state in memo:
                return memo[state]

            if word1[i] == word2[j]:
                memo[state] = helper(i+1, j+1)
                return memo[state]

            insert = helper(i, j+1)
            delete = helper(i+1, j)
            replace = helper(i+1, j+1)

            memo[state] = 1 + min(insert, delete, replace)
            return memo[state]

        return helper(0, 0)