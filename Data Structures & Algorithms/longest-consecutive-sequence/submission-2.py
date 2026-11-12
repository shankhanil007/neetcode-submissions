class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ## Approach 1:
        ## Sort the array
        ## 

        nums.sort()
        maxi = 0
        for itr in range(0, len(nums)):
            if itr == 0:
                lcs = 1
            elif nums[itr] - nums[itr-1] == 1:
                lcs += 1
            elif nums[itr] != nums[itr-1]:   ### If not equal -> reset lcs; If equal -> same lcs
                lcs = 1
            maxi = max(lcs, maxi)

        return maxi

        