class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        memo = {}

        def helper(idx):
            if idx >= n:
                return True

            if idx in memo:
                return memo[idx]

            for word in wordDict:
                l = len(word)
                if s[idx: idx+l] == word:
                    if helper(idx+l):
                        memo[idx] = True
                        return memo[idx]
            
            memo[idx] = False
            return memo[idx]

        return helper(0)