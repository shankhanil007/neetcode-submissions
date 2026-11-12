class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2:
            return False

        n = len(nums)
        target = sum(nums)//2
        dp = [[False] * (target+1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = True

        for i in range(1, n):
            for j in range(1, target+1):
                if nums[i] <= j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i]] ### Till index i can you make the target
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[n-1][target]


