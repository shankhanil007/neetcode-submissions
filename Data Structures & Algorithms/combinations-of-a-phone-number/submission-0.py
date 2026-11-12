class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        ans = []
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

        def helper(idx, curr_combi):

            if idx == len(digits):
                if curr_combi:
                    ans.append(curr_combi)
                return

            chars = digitToChar[digits[idx]]
            for ch in chars:
                curr_combi += ch
                helper(idx+1, curr_combi)
                curr_combi = curr_combi[:-1]
        
        helper(0, "")

        return ans