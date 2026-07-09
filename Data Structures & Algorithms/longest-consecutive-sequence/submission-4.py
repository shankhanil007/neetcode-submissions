class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ## Approach 1:
        ## Sort the array
        ## compare consecutive elements

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


        ## Approach 2
        
        ## IMP Start of sequence = (n-1) should not be present

        unique = set(nums)
        hmap = {}
        maxi = 0

        for elem in unique:
            hmap[elem] = hmap.get(elem,0) + 1
        for elem in unique:
            if hmap[elem-1] == 0:
                lcs = 1
                nxt = elem + 1
                while true:
                    if hmap[nxt] == 0:
                        break
                    else:
                        lcs += 1
                maxi = max(lcs, maxi)
        return maxi
            

        