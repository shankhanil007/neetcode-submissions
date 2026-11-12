class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = 101
        profit = [0]*len(prices)
        for i, price in enumerate(prices):
            if price <= min_val:
                min_val = price
            profit[i] = (price-min_val) if i==0 else max(profit[i-1], price-min_val)
        return profit[len(profit)-1]
