class Solution:
    
    def twoSum(self, nums, target, idx, ans):
        l, h = idx, len(nums)-1
        while l < h:
            result = nums[l] + nums[h]
            if result == target:
                ans.append([nums[l], nums[h], -target])
                l += 1
                h -= 1
                while l < h and nums[l] == nums[l-1]:
                    l += 1
                while l < h and nums[h] == nums[h+1]:
                    h -= 1
            elif result < target:
                l += 1
            else:
                h -= 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums = sorted(nums)
        seen = None
        for idx, num in enumerate(nums):
            if num == seen:
                continue
            seen = num
            res = self.twoSum(nums, -num, idx+1, ans)
        return ans


