class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # hmap = defaultdict(int)
        # for i, num in enumerate(nums):
        #     if hmap.get(num, -1) >= 0:
        #         if (i - hmap[num]) <= k:
        #             return True
        #     hmap[num] = i
        # return False

        i, j = 0, 0
        unique = set()
        while j < len(nums):
            while j < len(nums) and j <= (i+k):
                if nums[j] in unique:
                    return True
                else:
                    unique.add(nums[j])
                j += 1
            unique.remove(nums[i])
            i += 1
        return False
            

            