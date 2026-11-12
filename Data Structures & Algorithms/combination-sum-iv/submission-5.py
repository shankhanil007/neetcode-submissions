class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}

        def helper(curr_target):

            if curr_target < 0:
                return 0
            if curr_target == 0:
                return 1

            if curr_target in memo:
                return memo[curr_target]
            
            combs = 0
            for num in nums:
                curr_target -= num
                combs += helper(curr_target)
                curr_target += num

            memo[curr_target] = combs
            return memo[curr_target]
        
        return helper(target)

