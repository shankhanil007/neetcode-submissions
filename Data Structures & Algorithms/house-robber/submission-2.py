class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for idx in range(1, len(nums)):
            if idx == 1:
                dp[idx] = max(nums[1], dp[0])
            else:
                dp[idx] = max(nums[idx] + dp[idx-2], dp[idx-1])
        return dp[-1]