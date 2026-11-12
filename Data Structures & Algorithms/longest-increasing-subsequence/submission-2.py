class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1] * len(nums)
        maxi = 1

        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):     ### 2, 5, 4, 3 to process 2 we need to check for all combinations. 
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    maxi = max(maxi, dp[i])
        return maxi


### TODO: check recursion tree to DP