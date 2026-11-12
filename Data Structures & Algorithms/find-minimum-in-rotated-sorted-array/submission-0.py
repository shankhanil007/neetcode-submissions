class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, h = 0, len(nums)-1
        ans = 1000000
        while l <= h:
            mid = (l+h)//2
            print(mid)
            if nums[mid] > nums[h]:
                l = mid + 1
            elif nums[mid] <= nums[h]:
                ans = min(ans, nums[mid])
                h = mid - 1
        return ans
