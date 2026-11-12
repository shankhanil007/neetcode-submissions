class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.ans = []

        def helper(curr_list, idx, nums):

            if idx == len(nums):
                self.ans.append(curr_list[:])
                return
            
            # print(nums[idx])
            curr_list.append(nums[idx])
            helper(curr_list, idx+1, nums)
            curr_list.pop()
            helper(curr_list, idx+1, nums)
        
            return
        
        helper([], 0, nums)
        return self.ans
