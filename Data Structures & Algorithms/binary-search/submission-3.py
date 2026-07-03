class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        s, l = 0, len(nums)-1
        while s <= l:
            mid = (s+l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                s = mid + 1
            else: 
                l = mid - 1
        return -1