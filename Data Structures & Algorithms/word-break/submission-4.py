class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        dp = [-1] * (n+1) 

        def helper(start):

            if start == n:
                return True
            
            for word in wordDict:
                k = len(word)
                if s[start: start + k] == word:
                    if dp[start + k] != -1:
                        return bool(dp[start + k])
                    else:
                        if helper(start+k):
                            dp[start + k] = 1
                            return True
            dp[start] = 0
            return False

        if helper(0):
            return True
        return False
