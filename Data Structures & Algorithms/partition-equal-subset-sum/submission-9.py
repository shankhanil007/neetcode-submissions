class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        n = len(nums)
        target = total_sum // 2
        dp = [[False] * (total_sum + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = True

        dp[0][nums[0]] = True

        for i in range(1,n):
            for j in range(1, target+1):
                dp[i][j] = dp[i-1][j - nums[i]] or dp[i-1][j]

        return dp[n-1][target]