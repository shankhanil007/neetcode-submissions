class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        l, r = 0, n-1

        while l <= r:
            mid = (l+r)//2
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                return mid

        return -1