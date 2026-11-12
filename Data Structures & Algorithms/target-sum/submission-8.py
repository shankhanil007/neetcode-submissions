class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        memo = {}

        def helper(idx, curr_sum):

            if idx >= n:
                if curr_sum == target:
                    return 1
                return 0
            
            state = (idx, curr_sum)
            if state in memo:
                return memo[state]

            ways = 0
            ways += helper(idx+1, curr_sum + nums[idx])
            ways += helper(idx+1, curr_sum - nums[idx])

            memo[state] = ways
            return ways

        return helper(0, 0)


             
            