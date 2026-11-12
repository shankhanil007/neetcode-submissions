class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = defaultdict(int)
        for num in nums:
            hmap[num] += 1
        
        for key, val in hmap.items():
            if val > (len(nums)/2):
                return key