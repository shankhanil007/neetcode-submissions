class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        memo = {}

        def helper(idx, curr_sum):
            if idx == n:
                if curr_sum == target:
                    return 1
                else:
                    return 0

            state = (idx, curr_sum)
            if state in memo:
                return memo[state]

            add = helper(idx+1, curr_sum + nums[idx])
            sub = helper(idx+1, curr_sum - nums[idx])
            memo[state] = add + sub
            
            return memo[state]

        return helper(0, 0)
