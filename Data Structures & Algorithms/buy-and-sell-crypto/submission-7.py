class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        maxi = 0
        for price in prices:
            profit = 0
            while stack and stack[-1][0] < price:
                last = stack[-1]
                stack.pop()
                curr_profit = last[1] + (price - last[0])
                profit = max(curr_profit, profit)
            maxi = max(profit, maxi)
            stack.append((price, profit))
        return maxi