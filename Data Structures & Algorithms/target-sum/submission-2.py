class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        memo = {}

        def helper(idx, amt):

            if idx >= n:
                if amt == 0:
                    return 1
                else:
                    return 0

            state = (idx, amt)
            if state in memo:
                return memo[state]

            opt1 = helper(idx+1, amt - nums[idx])
            opt2 = helper(idx+1, amt + nums[idx])
            memo[state] = opt1 + opt2
            
            return memo[state]

        return helper(0, target)