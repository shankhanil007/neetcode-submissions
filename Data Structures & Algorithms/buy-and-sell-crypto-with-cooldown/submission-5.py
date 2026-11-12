class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        memo = {}

        def helper(idx, can_buy):

            if idx >= n:
                return 0
            
            state = (idx, can_buy)
            if state in memo:
                return memo[state]

            if can_buy:
                option1 = -prices[idx] + helper(idx+1, False)
                option2 = helper(idx+1, True)
                memo[state] = max(option1, option2) 

            else:
                option1 = prices[idx] + helper(idx+2, True)
                option2 = helper(idx+1, False)
                memo[state] = max(option1, option2) 
            
            return memo[state]
        
        return helper(0, True)
