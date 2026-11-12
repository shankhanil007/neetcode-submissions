class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        candidates.sort()

        def helper(cur_sum, cur_list, cur_idx):

            if cur_sum == target:
                ans.append(cur_list[:])
                return

            for itr in range(cur_idx, len(candidates)):
                if itr > cur_idx and candidates[itr] == candidates[itr - 1]:
                    continue
                cur_sum += candidates[itr]
                if cur_sum > target:
                    return
                cur_list.append(candidates[itr])
                helper(cur_sum, cur_list, itr + 1)
                cur_list.pop()
                cur_sum -= candidates[itr]

        helper(0, [], 0)
        return ans

                