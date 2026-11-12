class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        ans = []

        def helper(idx, curr):
            if idx >= len(digits):
                ans.append(curr[:])
                return

            chars = digitToChar[digits[idx]]
            for ch in chars:
                curr += ch
                helper(idx+1, curr)
                curr = curr[:-1]
        
        if not digits:
            return []
            
        helper(0, "")
        return ans