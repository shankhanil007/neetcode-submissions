class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        n = len(candidates)
        candidates.sort()

        def helper(idx, curr, curr_sum):
           
            if curr_sum == target:
                ans.append(curr[:])
                return
            if curr_sum > target:
                return 
            if idx >= n:
                return 
            

            curr.append(candidates[idx])
            curr_sum += candidates[idx]
            helper(idx+1, curr, curr_sum)
            curr.pop()
            curr_sum -= candidates[idx]
            
            temp = candidates[idx]
            idx += 1
            while idx < n and candidates[idx] == temp:
                idx += 1
            helper(idx, curr, curr_sum)

        
        helper(0, [], 0)
        return ans