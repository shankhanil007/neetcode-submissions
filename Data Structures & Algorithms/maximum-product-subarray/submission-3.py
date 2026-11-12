class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        maxi = - float('inf')

        for i in range(n):
            dp[i][i] = nums[i]
            maxi = max(maxi, dp[i][i])

        
        for length in range(2, n+1):
            for row in range(n):
                col = row + length - 1
                if col < n:
                    dp[row][col] = dp[row][col-1] * nums[col]
                    maxi = max(maxi, dp[row][col])

        return maxi