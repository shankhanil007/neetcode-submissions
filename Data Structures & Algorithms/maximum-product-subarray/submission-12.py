class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # n = len(nums)
        # dp = [[0] * n for _ in range(n)]
        # maxi = - float('inf') #### IIIMMPP handle -ve solutions

        # for i in range(n):
        #     dp[i][i] = nums[i]
        #     maxi = max(maxi, dp[i][i])  #### IIIMMPP to handle single element arrays
        
        # for length in range(2, n+1):
        #     for row in range(n):
        #         col = row + length - 1
        #         if col < n:
        #             dp[row][col] = dp[row][col-1] * nums[col]
        #             maxi = max(maxi, dp[row][col])

        # return maxi


        curr_max, curr_min = 1, 1
        res = nums[0]

        for num in nums:
            # if num == 0:
            #     curr_max = 1
            #     curr_min = 1

            tmp = num * curr_max  ### curr_max should be for the i-1 element
            curr_max = max(num * curr_max, num * curr_min, num) ### [1, 8] or [-1, -8] or [-8, 8]
            curr_min = min(tmp, num * curr_min, num)

            res = max(res, curr_max)

        return res