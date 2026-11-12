class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = 101
        max_profit = 0
        for i, price in enumerate(prices):
            if price <= min_val:
                min_val = price
            max_profit = max(max_profit, price-min_val)
        return max_profit