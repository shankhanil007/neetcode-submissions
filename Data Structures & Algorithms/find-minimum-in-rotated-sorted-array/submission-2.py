class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, h = 0, len(nums)-1
        while l < h:
            mid = (l+h)//2
            if nums[mid] > nums[h]:
                l = mid + 1
            else:
                h = mid
        return nums[l]

        l, h = 0, len(nums)-1
        while l <= h:
            mid = (l+h)//2
            print(mid)
            if nums[mid] > nums[h]:
                l = mid + 1
            elif nums[mid] < nums[h]:
                h = mid
        return nums[h]
