class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        cmax, cmin = 1, 1
        ans = -float('inf')

        for i in range(len(nums)):
            tmp = nums[i] * cmax
            cmax = max(nums[i], nums[i] * cmax, nums[i] * cmin)
            cmin = min(nums[i], tmp, nums[i] * cmin)
            ans = max(ans, cmax)
        
        return ans