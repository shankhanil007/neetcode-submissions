class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)

        if l1 + l2 != l3:
            return False

        memo = {}

        def helper(i, j):

            if i + j == l3:
                return True

            state = (i, j)
            if state in memo:
                return memo[state]

            if i < l1 and s1[i] == s3[i+j] and helper(i+1, j):
                memo[state] = True
                return memo[state]
            if j < l2 and s2[j] == s3[i+j] and helper(i, j+1):
                memo[state] = True
                return memo[state]

            memo[state] = False
            return memo[state]

        return helper(0, 0)

