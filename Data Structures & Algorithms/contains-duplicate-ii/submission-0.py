class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap = defaultdict(int)
        for i, num in enumerate(nums):
            if hmap.get(num, -1) >= 0:
                if (i - hmap[num]) <= k:
                    return True
            hmap[num] = i
        return False
            