class Solution:
    
    def twoSum(self, nums, target, idx):
        pairs = []
        l, h = idx, len(nums)-1
        while l < h:
            result = nums[l] + nums[h]
            if result == target:
                pairs.append([nums[l], nums[h]])
                low = nums[l]
                high = nums[h]
                while len(nums) < l < h and nums[l] == low:
                    l += 1
                while l < h and nums[h] == high:
                    h -= 1
            elif result < target:
                l += 1
            else:
                h -= 1
        return pairs

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums = sorted(nums)
        seen = None
        for idx, num in enumerate(nums):
            if num == seen:
                continue
            seen = num
            res = self.twoSum(nums, num * -1, idx+1)
            if res:
                for elem in res:
                    elem.append(num)
                    ans.append(elem)
        return ans


