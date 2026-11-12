class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1

        ans = 0
        for idx, num in enumerate(nums):
            if not hmap.get(num-1, 0):
                length = 1
                while True:
                    nxt = num + length
                    if hmap.get(nxt, 0):
                        length += 1
                    else:
                        ans = max(ans, length)
                        break
        return ans