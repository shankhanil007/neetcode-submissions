class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []

        def helper(l, r, curr):
            if l == r == n:
                ans.append(curr)
                return

            if l < n:
                curr += '('
                helper(l+1, r, curr)
                curr = curr[:-1]
            if r < n and r<l:
                curr += ')'
                helper(l, r+1, curr)
                curr = curr[:-1]
        
        helper(0, 0, "")
        return ans
