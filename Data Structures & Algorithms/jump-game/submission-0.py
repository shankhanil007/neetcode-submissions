class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        maxReach = 0
        for idx, num in enumerate(nums):
            if idx > maxReach:
                return False
            if idx == len(nums) - 1:
                return True
            maxReach = max(maxReach, idx + num)
        
        return False