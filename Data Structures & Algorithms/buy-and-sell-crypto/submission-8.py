class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = prices[0]
        maxi = 0
        for i in range(1, len(prices)):
            minVal = min(prices[i], minVal)
            currProfit = prices[i] - minVal
            maxi = max(currProfit, maxi)
            
        return maxi