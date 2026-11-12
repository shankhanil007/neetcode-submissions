class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for amt in range(1, amount+1):
            for i in range(len(coins)): 
                if coins[i] <= amt:
                    if dp[amt - coins[i]] != -1:
                        dp[amt] = min(dp[amt], 1 + dp[amt - coins[i]])

        return -1 if dp[amount] == float('inf') else dp[amount]

