class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        # self.maxi = 0 ### Using mutable instance variables like these prevents you from caching subproblems.
        # self.buy = 0

        memo = {}

        def helper(idx, can_buy):
            if idx >= n:
                return 0

            state = (idx, can_buy)
            if state in memo:
                return memo[state]

            if can_buy:
                profitA =  -prices[idx] + helper(idx+1, False)
                profitB = 0 + helper(idx+1, True)
                memo[state] = max(profitA, profitB) 
            
            else:
                profitA =  +prices[idx] + helper(idx+2, True)
                profitB = 0 + helper(idx+1, False)
                memo[state] = max(profitA, profitB) 
                
            return memo[state]
                
        return helper(0, True)