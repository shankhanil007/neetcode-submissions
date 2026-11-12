class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        dp = [False] * (n+1)
        # memo = {}
        dp[n] = True

        for idx in range(n-1, -1, -1):
            for i in range(len(wordDict)):
                l = len(wordDict[i])
                if s[idx:idx+l] == wordDict[i] and dp[idx+l]:
                    dp[idx] = True

        return dp[0]
