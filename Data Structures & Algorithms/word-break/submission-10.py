class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        memo = {}

        def dfs(idx):
            
            if idx == n:
                return True

            if idx in memo.keys():
                return memo[idx]

            for word in wordDict:
                if (idx + len(word) <= n) and s[idx : idx + len(word)] == word:
                    if dfs(idx + len(word)):
                        memo[idx] = True
                        return True
            memo[idx] = False
            return False

        return dfs(0)

