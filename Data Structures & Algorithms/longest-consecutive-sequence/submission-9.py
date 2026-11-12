class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ## Approach 1:
        ## Sort the array
        ## compare consecutive elements

        # nums.sort()
        # maxi = 0
        # for itr in range(0, len(nums)):
        #     if itr == 0:
        #         lcs = 1
        #     elif nums[itr] - nums[itr-1] == 1:
        #         lcs += 1
        #     elif nums[itr] != nums[itr-1]:   ### If not equal -> reset lcs; If equal -> same lcs
        #         lcs = 1
        #     maxi = max(lcs, maxi)

        # return maxi


        ## Approach 2
        
        ## IMP Start of sequence = (n-1) should not be present

        hmap = {}
        maxi = 0  ## for empty inputs

        for elem in nums:
            hmap[elem] = hmap.get(elem,0) + 1
        for elem in hmap.keys():
            if hmap.get(elem-1, 0) == 0:
                lcs = 1
                while True:
                    nxt = elem + lcs
                    print(nxt)
                    if hmap.get(nxt, 0):
                        lcs += 1
                    else:
                        break
                maxi = max(lcs, maxi)
        return maxi



            
            
            
            
            
            
            
            
            
            
            
        

        