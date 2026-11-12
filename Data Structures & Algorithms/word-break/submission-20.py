class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True

        for idx in range(n-1, -1, -1):
            for word in wordDict:
                l = len(word)
                if s[idx: idx+l] == word:
                    if dp[idx+l]:
                        dp[idx] = True
                        break
                    

        return dp[0]