class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = defaultdict(int)
        for num in nums:
            if hmap.get(num,0) != 0:
                return True
            hmap[num] += 1
        return False
        