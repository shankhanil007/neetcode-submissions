class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = 101
        profit = [0]*(len(prices)+1)
        for i, price in enumerate(prices):
            if price < min_val:
                min_val = price
            profit[i+1] = max(profit[i], price-min_val)
        return profit[len(profit)-1]
