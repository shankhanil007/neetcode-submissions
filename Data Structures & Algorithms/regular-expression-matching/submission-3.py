class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        memo = {}

        def helper(i, j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            state = (i, j)
            if state in memo:
                return memo[state]

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if (j + 1) < len(p) and p[j + 1] == "*":
                memo[state] = (helper(i, j + 2) or (match and helper(i + 1, j))) 
                return memo[state]

            if match:
                memo[state] = helper(i + 1, j + 1)
                return memo[state] 

            memo[state] = False
            return memo[state]

        return helper(0, 0)
