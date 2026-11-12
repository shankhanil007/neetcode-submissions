class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # maxReach = 0
        # for idx, num in enumerate(nums):
        #     if idx > maxReach:
        #         return False
        #     if idx == len(nums) - 1:
        #         return True
        #     maxReach = max(maxReach, idx + num)
        
        # return False

        memo = {}

        def dfs(idx):
            if idx >= len(nums)-1:
                return True
            
            state = idx
            if state in memo:
                return memo[state]

            for i in range(1, nums[idx]+1):
                nxt = idx + i
                if dfs(nxt):
                    memo[idx] = True
                    return memo[idx]

            memo[idx] = False
            return memo[idx]

        return dfs(0)