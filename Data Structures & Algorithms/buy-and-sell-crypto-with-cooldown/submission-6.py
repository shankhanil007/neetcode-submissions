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
                opt1 = -prices[idx] + helper(idx+1, False)
                opt2 = helper(idx+1, can_buy)
            else:
                opt1 = +prices[idx] + helper(idx+2, True)
                opt2 = helper(idx+1, can_buy)

            memo[state] = max(opt1, opt2)
            return memo[state] 

        return helper(0, True)
            
            