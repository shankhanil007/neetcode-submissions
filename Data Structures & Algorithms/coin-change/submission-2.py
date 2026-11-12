class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        #### Why greedy fails

        ### recursive memoization need from visual graph

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for amt in range(1, amount + 1):
            for itr in range(0, len(coins)): ### IIMMMPP need to check the amount for all coins. As we are building the amounnt from bottom up
                if (amt - coins[itr]) >= 0:
                    dp[amt] = min(dp[amt], 1+dp[amt - coins[itr]])

        return -1 if dp[amount] == float('inf') else dp[amount] 