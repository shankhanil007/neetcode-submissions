class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        memo = {}

        def helper(idx):
            if idx >= n:
                return True

            if idx in memo:
                return memo[idx]
            
            for i in range(len(wordDict)):
                l = len(wordDict[i])
                if n-idx >= l:
                    if s[idx:idx+l] == wordDict[i]:
                        if helper(idx+l):
                            memo[idx] = True
                            return memo[idx]

            memo[idx] = False
            return memo[idx]

        return helper(0)
