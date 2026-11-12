class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        l1 = len(s)
        l2 = len(t)
        memo = {}

        def helper(i, j):
            if j >= l2:
                return 1
            if i >= l1:
                return 0

            state = (i, j)
            if state in memo:
                return memo[state]

            if s[i] == t[j]:
                memo[state] = helper(i+1, j+1) + helper(i+1, j)
                
            else:
                memo[state] = helper(i+1, j)
            
            return memo[state]
        
        return helper(0, 0)

