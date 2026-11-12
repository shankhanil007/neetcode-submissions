class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums.sort()  # Step 1: Sort to group duplicates (Crucial!)

        def helper(cur_idx, cur_list):
            # Step 2: Every step is a valid subset!
            # Append a copy of cur_list to ans right here
            ans.append(cur_list[:])
            
            # Step 3: Loop through remaining candidates
            for itr in range(cur_idx, len(nums)):
                
                # Step 4: The identical duplicate check from Combination Sum II
                if itr > cur_idx and nums[itr] == nums[itr - 1]:
                    continue
                
                # Step 5: standard backtrack steps
                cur_list.append(nums[itr])
                helper(itr+1, cur_list)
                cur_list.pop()
                
        helper(0, [])
        return ans