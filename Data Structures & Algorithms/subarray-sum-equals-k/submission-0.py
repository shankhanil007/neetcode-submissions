class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix_sum = 0
        hmap = {}
        hmap[0] = 1
        count = 0
        for idx, elem in enumerate(nums):
            prefix_sum += elem
            if hmap.get(prefix_sum-k, 0):
                count += hmap[prefix_sum-k]
            hmap[prefix_sum] = hmap.get(prefix_sum, 0) + 1
                    
        return count