class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hmap = {}
        for idx, num in enumerate(nums):
            rem = target - num
            if rem in hmap:
                return [hmap[rem], idx]
            hmap[num] = idx