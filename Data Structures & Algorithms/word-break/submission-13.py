class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        memo = {}

        def helper(idx):
            if idx >=n :
                return True
            
            if idx in memo.keys():
                return memo[idx]

            for word in wordDict:
                if s[idx: idx+len(word)] == word:
                    if helper(idx + len(word)):
                        memo[idx] = True
                        return True

            memo[idx] = False
            return False

        return helper(0)