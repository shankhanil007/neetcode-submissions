class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        cur_max, cur_min = 1, 1
        ans = nums[0]

        for elem in nums:
            tmp = elem * cur_max
            cur_max = max(tmp, elem * cur_min, elem)
            cur_min = min(tmp, elem * cur_min, elem)
            ans = max(ans, cur_max)

        return ans