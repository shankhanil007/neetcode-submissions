class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []
        n = len(nums)

        def helper(idx, curr, curr_sum):
            if idx >= n:
                if curr_sum == target:
                    ans.append(curr[:])
                return 
            if curr_sum > target:
                return 



            curr.append(nums[idx])
            curr_sum += nums[idx]
            helper(idx, curr, curr_sum)
            curr.pop()
            curr_sum -= nums[idx]
            helper(idx+1, curr, curr_sum)

        
        helper(0, [], 0)
        return ans