class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n = len(nums)
        ans = []

        def helper(idx, curr, rem):
            if rem == 0:
                ans.append(curr[:])
                return
            if rem < 0 or idx >= n:
                return
            curr.append(nums[idx])
            helper(idx, curr, rem - nums[idx])
            curr.pop()
            helper(idx+1, curr, rem)

        helper(0, [], target)
        return ans


