class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums.sort()
        ans = [0] * len(nums)
        for itr in range(0, len(nums)):
            if itr == 0:
                ans[itr] = 1
            elif nums[itr] - nums[itr-1] == 1:
                ans[itr] = ans[itr-1] + 1
            elif nums[itr] == nums[itr-1]:
                ans[itr] = ans[itr-1]
            else:
                ans[itr] = 1
        maxi = 0
        for elem in ans:
            maxi = max(elem, maxi)
        return maxi