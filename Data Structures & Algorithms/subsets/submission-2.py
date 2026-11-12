class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        def helper(curr_list, idx, nums):

            if idx == len(nums):
                ans.append(curr_list[:]) ## IMP Pass a copy of the list
                return
            
            curr_list.append(nums[idx])
            helper(curr_list, idx+1, nums)
            curr_list.pop()
            helper(curr_list, idx+1, nums)
        
            return
        
        helper([], 0, nums)
        return ans
