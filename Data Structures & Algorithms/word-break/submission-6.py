class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        dp = {n: True}

        def helper(start):
            if start in dp:
                return dp[start]
            for word in wordDict:
                if s[start: start + len(word)] == word:
                    if helper(start+len(word)):
                        dp[start] = True
                        return True
            dp[start] = False
            return False

        if helper(0):
            return True
        return False
