class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * len(nums)
        mul = 1
        for i in range(1, len(nums)):
            prefix[i] = mul * nums[i-1]
            mul = prefix[i]

        mul = 1
        for i in range(len(nums)-1, -1, -1):
            prefix[i] = mul * prefix[i]
            mul *= nums[i]

        return prefix