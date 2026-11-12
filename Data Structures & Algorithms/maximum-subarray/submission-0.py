class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ans = -float('inf')
        add = 0

        for elem in nums:
            add += elem
            ans = max(ans, add)
            if add < 0:
                add = 0

        return ans





    