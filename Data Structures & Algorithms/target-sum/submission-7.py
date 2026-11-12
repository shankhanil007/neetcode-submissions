class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # n = len(nums)
        # memo = {}

        # def helper(idx, total):
        #     if idx >= n:
        #         if total == 0:  ### total == 0 not total === target
        #             return 1 
        #         else:
        #             return 0

        #     state = (idx, total)
        #     if state in memo:
        #         return memo[state]

        #     opt1 = helper(idx+1, total-nums[idx])
        #     opt2 = helper(idx+1, total+nums[idx])

        #     memo[state] = opt1 + opt2
        #     return memo[state]

        # return helper(0, target)


        ################# DP based solution #################

        n = len(nums)
        dp = [defaultdict(int) for _ in range(n+1)]
        dp[0][0] = 1

        for row in range(n):
            for cur_sum, count in dp[row].items():
                dp[row+1][cur_sum + nums[row]] += dp[row][cur_sum]
                dp[row+1][cur_sum - nums[row]] += dp[row][cur_sum]

        return dp[n][target]






