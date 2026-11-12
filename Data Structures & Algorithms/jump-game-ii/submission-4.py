class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        memo = {}
        
        def helper(idx):
            if idx >= n-1:
                return 0

            if idx in memo:
                return memo[idx]

            min_jumps = float('inf')
            steps = nums[idx]
            for step in range(1, steps+1):
                min_jumps = min(min_jumps, 1 + helper(idx+step))
            
            memo[idx] = min_jumps
            return min_jumps

        return helper(0)


