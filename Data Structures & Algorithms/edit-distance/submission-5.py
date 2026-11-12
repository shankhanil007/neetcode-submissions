class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        l1 = len(word1)
        l2 = len(word2)


        memo = {}

        def helper(i, j):
            
            if i >= l1 and j >= l2:
                return 0
            
            if i >= l1:
                return l2 - j
            if j >= l2:
                return l1 - i 

            state = (i, j)
            if state in memo:
                return memo[state]

            ops = 0
            if word1[i] == word2[j]:
                ops += helper(i+1, j+1)

            else:
                insert = helper(i, j+1)
                delete = helper(i+1, j)
                update = helper(i+1, j+1)
                ops = 1 + min(insert, delete, update)

            memo[state] = ops
            return ops

        return helper(0, 0)