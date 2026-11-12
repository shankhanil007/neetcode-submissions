class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob_linear(arr):
            rob1, rob2 = 0, 0
            for money in arr:
                curr = max(money + rob1, rob2)
                rob1 = rob2 
                rob2 = curr
            return rob2 
        
        if len(nums) == 1:
            return nums[0]
            
        return max(rob_linear(nums[0: -1]), rob_linear(nums[1: ]))
