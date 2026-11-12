class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [1] * len(nums) 

        for idx in range(1,len(nums)):
            ans[idx] = ans[idx-1] * nums[idx-1]

        postfix = nums[len(nums)-1]
        for idx in range(len(nums)-2, -1, -1):
            ans[idx] = ans[idx] * postfix
            postfix *= nums[idx]
            
        return ans