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

            nxt = idx + 1
            while nxt < n and nums[nxt] == nums[idx]:
                nxt += 1
            helper(nxt, curr)

        helper(0, [])
        return ans