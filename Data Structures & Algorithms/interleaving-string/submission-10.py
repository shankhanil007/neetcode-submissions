class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        l1 = len(s1)
        l2 = len(s2)

        if len(s3) != l1 + l2:
            return False

        memo = {}

        def helper(i, j):
            
            if i >= l1 and j >= l2:
                return True

            state = (i, j)
            if state in memo:
                return memo[state]

            if i < l1 and s1[i] == s3[i+j]:
                if helper(i+1, j):
                    memo[state] = True
                    return True
            if j < l2 and s2[j] == s3[i+j]:  ###  less condition and if and if not elif
                if helper(i, j+1):
                    memo[state] = True
                    return True

            memo[state] = False
            return False

        return helper(0, 0)