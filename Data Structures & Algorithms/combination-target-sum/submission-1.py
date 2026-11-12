class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []
        nums.sort()

        def helper(curr_sum, curr_idx, curr_list):

            if curr_sum == target:
                ans.append(curr_list[:])
                return

            for itr in range(curr_idx, len(nums)):
                curr_sum += nums[itr]
                if curr_sum > target:
                    break
                curr_list.append(nums[itr])
                helper(curr_sum, itr, curr_list)
                curr_list.pop()
                curr_sum -= nums[itr]
            
        helper(0, 0, [])
        return ans
