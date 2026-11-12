class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        dp = [[float('inf')] * (amount+1) for _ in range(n+1)]

        for row in range(n+1):
            dp[row][0] = 0

        for row in range(1, n+1):
            for amt in range(1, amount+1):
                not_take = dp[row-1][amt]
                take = float('inf')
                if amt >= coins[row-1]:
                    take = 1 + dp[row][amt-coins[row-1]]
                dp[row][amt] = min(take, not_take)
        
        return -1 if dp[-1][-1] == float('inf') else dp[-1][-1]