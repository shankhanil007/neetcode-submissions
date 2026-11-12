class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []
        nums.sort()

        def helper(cur_sum, cur_list, idx):

            if cur_sum == target:
                ans.append(cur_list.copy())
                return
            
            for itr in range(idx, len(nums)):
                cur_sum += nums[itr]
                if cur_sum > target:
                    return
                cur_list.append(nums[itr])
                print(cur_list)
                helper(cur_sum, cur_list, itr)
                cur_list.pop()
                cur_sum -= nums[itr]
            
        helper(0, [], 0)
        return ans
