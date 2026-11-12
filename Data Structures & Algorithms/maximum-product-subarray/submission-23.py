class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        cmax, cmin = 1, 1
        ans = -float('inf')

        for i in range(len(nums)):
            temp1 = nums[i] * cmax
            temp2 = nums[i] * cmin
            ans = max(ans, nums[i], temp1, temp2)
            cmax = max(nums[i], temp1, temp2)
            cmin = min(nums[i], temp1, temp2) 
        
        return ans