class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        max_profit = 0
        for price in prices:
            min_val = min(min_val, price)
            max_profit = max(max_profit, price-min_val)
        return max_profit