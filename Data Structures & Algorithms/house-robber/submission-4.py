class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # dp = [0] * len(nums)
        # dp[0] = nums[0]

        # for idx in range(1, len(nums)):
        #     if idx == 1:
        #         dp[idx] = max(nums[1], dp[0])
        #     else:
        #         dp[idx] = max(nums[idx] + dp[idx-2], dp[idx-1])
        # return dp[-1]

        

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        rob1 = nums[0]
        rob2 = max(nums[0], nums[1])

        for itr in range(2, len(nums)):
            curr = max(nums[itr] + rob1, rob2)
            rob1 = rob2
            rob2 = curr
        return rob2
