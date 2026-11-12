class Solution:
    def jump(self, nums: List[int]) -> int:
        
        memo = {}

        def dfs(idx):
            if idx >= len(nums) - 1:
                return 0
            
            state = idx
            if state in memo:
                return memo[state]

            minSteps = float('inf')
            for i in range(1, nums[idx]+1):
                steps = dfs(idx + i)
                minSteps = min(minSteps, steps)
            
            memo[state] = 1 + minSteps

            return memo[state] 

        return dfs(0)
