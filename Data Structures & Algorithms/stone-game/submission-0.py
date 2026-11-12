class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        memo = {}

        def helper(start, end):

            if start == end:
                return piles[start]

            state = (start, end)
            if state in memo:
                return memo[state]
            
            gainA = piles[start] - helper(start+1, end)
            gainB = piles[end] - helper(start, end-1)
            memo[state] = max(gainA, gainB)
            return memo[state]

        return helper(0, len(piles)-1) > 0