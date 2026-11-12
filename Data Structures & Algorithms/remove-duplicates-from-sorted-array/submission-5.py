class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
                
        ####### i is the counter that conveys that the numbers before it are all distinct
        
        if len(nums) == 1:
            return 1
        
        i, j = 1, 1

        while j<len(nums):
            if nums[i-1] != nums[j]:
                nums[i] = nums[j]
                i += 1
            j += 1

        return i