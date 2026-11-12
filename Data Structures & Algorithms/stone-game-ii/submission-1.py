class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        memo = {}

        def helper(start, M):

            if start >= len(piles):
                return 0

            state = (start, M)
            if state in memo:
                return memo[state]
            
            maxi = -float("inf")
            for X in range(1, 2*M+1):
                gain = sum(piles[start: start+X]) - helper(start+X, max(M, X))
                maxi = max(maxi, gain)
            
            memo[state] = maxi
            return memo[state]

        return (helper(0, 1) + sum(piles))//2