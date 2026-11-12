class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        ans = []

        def helper(idx, curr_sum, curr):
            if curr_sum == target:
                ans.append(curr[:])
                return
            
            if idx >= len(candidates) or curr_sum > target:
                return

            curr_sum += candidates[idx]
            curr.append(candidates[idx])
            helper(idx+1, curr_sum, curr)
            curr_sum -= candidates[idx]
            curr.pop()
            temp = idx
            idx += 1

            while idx < len(candidates) and candidates[idx] == candidates[temp]:
                idx += 1
            helper(idx, curr_sum, curr)
            
            return 

        helper(0, 0, [])

        return ans
            

