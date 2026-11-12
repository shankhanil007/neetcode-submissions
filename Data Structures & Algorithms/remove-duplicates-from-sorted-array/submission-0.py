class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        i, j, k = 0, 1, 1

        while j<len(nums):
            if nums[i] == nums[j]:
                pass
            else:
                nums[k] = nums[j]
                i += 1
                k += 1
            j += 1

        return i+1