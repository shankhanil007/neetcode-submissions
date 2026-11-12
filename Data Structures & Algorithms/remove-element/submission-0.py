class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        nums[:] = sorted(nums, key=lambda x: (x == val, x))
        
        for i in range(0, len(nums)):
            if nums[i] == val:
                return i
        
        return len(nums)