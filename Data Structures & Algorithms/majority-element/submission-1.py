class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = defaultdict(int)
        maxi, res = 0, 0
        for num in nums:
            hmap[num] += 1
            if hmap[num] > maxi:
                maxi = hmap[num]
                res = num
        
        return res