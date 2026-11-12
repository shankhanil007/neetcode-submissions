class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        self.ans = [[]]

        def helper(idx, curr):
            if idx >= n:
                return 

            curr.append(nums[idx])
            self.ans.append(curr[:])
            helper(idx+1, curr)
            curr.pop()
            helper(idx+1, curr)

        helper(0, [])
        return self.ans