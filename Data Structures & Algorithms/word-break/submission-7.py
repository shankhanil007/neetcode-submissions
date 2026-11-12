class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        dp = {n: True}  ### TO ADD. EOS will always be True

        def helper(start):
            if start in dp:         ### TO Change
                return dp[start]    ### TO Change
            for word in wordDict:
                if s[start: start + len(word)] == word:
                    if helper(start+len(word)):
                        dp[start] = True    ### TO Add. If start matches and the remaining is True. Then the start is True
                        return True
            dp[start] = False           ### TO Add
            return False

        if helper(0):
            return True
        return False
