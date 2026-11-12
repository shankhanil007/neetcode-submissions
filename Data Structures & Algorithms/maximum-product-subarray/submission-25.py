class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxVal, minVal = 1, 1
        ans = nums[0]

        for num in nums:
            temp = max(num, num * maxVal, num * minVal)
            minVal = min(num, num * maxVal, num * minVal)
            maxVal = temp
            ans = max(ans, maxVal)
            # if num == 0:
            #     maxVal, minVal = 1, 1

        return ans
