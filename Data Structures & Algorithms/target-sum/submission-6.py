class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        memo = {}

        def helper(idx, total):
            if idx >= n:
                if total == 0:
                    return 1
                else:
                    return 0

            state = (idx, total)
            if state in memo:
                return memo[state]

            opt1 = helper(idx+1, total-nums[idx])
            opt2 = helper(idx+1, total+nums[idx])

            memo[state] = opt1 + opt2
            return memo[state]

        return helper(0, target)