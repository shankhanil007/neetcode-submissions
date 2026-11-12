class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = True
        
        dp[0][nums[0]] = True #### IMMMPPP

        for i in range(1, n):
            for t in range(1, target+1):
                if nums[i] <= t:
                    dp[i][t] = dp[i-1][t] or dp[i-1][t-nums[i]] 
                else:
                    dp[i][t] = dp[i-1][t]
        return dp[n-1][target]