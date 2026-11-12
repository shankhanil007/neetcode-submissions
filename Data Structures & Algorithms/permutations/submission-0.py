class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        def helper(cur_idx, cur_list):

            if len(cur_list) == len(nums):
                ans.append(cur_list[:])
                return

            for pos in range(cur_idx, len(nums)):
                for itr in range(0, len(nums)):
                    if nums[itr] not in cur_list:
                        cur_list.append(nums[itr])
                        helper(pos+1, cur_list)
                        cur_list.pop()
            
        helper(0, [])
        return ans