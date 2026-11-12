class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        dp = [[float('inf')] * (amount+1) for _ in range(n)]

        for row in range(n):
            dp[row][0] = 0

        for amt in range(1, amount+1):
            for row in range(n):
                take = float('inf')
                if amt >= coins[row]:
                    take = 1 + dp[row][amt - coins[row]]
                not_take = dp[row-1][amt]
                dp[row][amt] = min(dp[row][amt], take, not_take)

        return -1 if dp[n-1][amount] == float('inf') else dp[n-1][amount]