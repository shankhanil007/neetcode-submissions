class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        ans = []
        nums.sort()

        def helper(idx, curr):
            if idx >= n:
                ans.append(curr[:])
                return

            curr.append(nums[idx])
            helper(idx+1, curr)
            curr.pop()

            temp = nums[idx]
            idx += 1
            while idx < n and nums[idx] == temp:
                idx += 1
            
            helper(idx, curr)
        
        helper(0, [])
        return ans
