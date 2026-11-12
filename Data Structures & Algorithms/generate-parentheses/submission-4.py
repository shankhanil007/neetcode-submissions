class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        start = 0
        end = 0
        ans = []

        def helper(start, end, cstring ):
            if start + end == 2*n:
                ans.append(cstring)
                return
            
            if start < n:
                cstring += "("
                helper(start+1, end, cstring)
                cstring = cstring[:-1]
            
            if end < start:
                cstring += ")"
                helper(start, end+1, cstring)
                cstring = cstring[:-1]
        helper(0,0, "")
        return ans
