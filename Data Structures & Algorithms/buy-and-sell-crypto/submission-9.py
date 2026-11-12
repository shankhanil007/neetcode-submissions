class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            profit = prices[i] - minSoFar
            ans = max(ans, profit)
            minSoFar = min(minSoFar, prices[i])
        return ans