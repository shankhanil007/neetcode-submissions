class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        dp = [float('inf')] * (amount+1)

        dp[0] = 0

        for amt in range(1, amount+1):
            for coin in coins:
                take = float('inf')
                if amt >= coin:
                    take = 1 + dp[amt - coin]
                not_take = dp[amt]
                dp[amt] = min(dp[amt], take, not_take)

        return -1 if dp[amount] == float('inf') else dp[amount]