class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        ######################## RECURSION ############
        # def dfs(curr_sum):

        #     if curr_sum == target:
        #         return 1
        #     if curr_sum > target:
        #         return 0

        #     ways = 0
        #     for num in nums:
        #         ways += dfs(curr_sum + num)

        #     return ways
    
        # return dfs(0)



        ######################## MEMOIZATION ############

        # memo = {}

        # def dfs(curr_sum):

        #     if curr_sum == target:
        #         return 1
        #     if curr_sum > target:
        #         return 0

        #     if curr_sum in memo:
        #         return memo[curr_sum]

        #     ways = 0
        #     for num in nums:
        #         ways += dfs(curr_sum + num)

        #     memo[curr_sum] = ways
        #     return memo[curr_sum]
        
        
        # return dfs(0)

        dp = [0] * (target+1)
        dp[0] = 1

        for curr_sum in range(1, target+1):
            for num in nums:
                if num <= curr_sum:
                    dp[curr_sum] += dp[curr_sum - num]

        return dp[target]

