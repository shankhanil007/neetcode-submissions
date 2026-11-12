class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        ans = []
        candidates.sort()

        def helper(idx, curr, rem):
            if rem == 0:
                ans.append(curr[:])
                return
            if rem < 0 or idx >= n:
                return
            curr.append(candidates[idx])
            helper(idx+1, curr, rem - candidates[idx])
            curr.pop()
            nxt = idx + 1
            while nxt < n and candidates[nxt] == candidates[idx]:
                nxt += 1
            helper(nxt, curr, rem)

        helper(0, [], target)
        return ans
