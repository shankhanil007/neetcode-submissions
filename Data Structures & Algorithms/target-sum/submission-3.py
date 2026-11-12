class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n+1)] #### DFdict(IIINNNTTT) IIIMMMPPP
        dp[0][0] = 1

        for row in range(n):
            for cur_sum, count in dp[row].items():  ### .items() IIIMMMMPPP
                dp[row+1][cur_sum - nums[row]] += dp[row][cur_sum] 
                dp[row+1][cur_sum + nums[row]] += dp[row][cur_sum]

        return dp[n][target] 