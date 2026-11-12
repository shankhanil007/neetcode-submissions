class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for row in range(1, n+1):
            for col in range(1, amount+1):
                dp[row][col] += dp[row-1][col] ## not take
                if coins[row-1] <= col:        ## take
                    dp[row][col] += dp[row][col - coins[row-1]]
        
        return dp[n][amount]
        