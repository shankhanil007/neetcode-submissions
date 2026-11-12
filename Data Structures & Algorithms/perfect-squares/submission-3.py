import sys

# Increase recursion depth limit so n = 10000 doesn't crash
sys.setrecursionlimit(20000)

class Solution:
    def numSquares(self, n: int) -> int:
        
        memo = {}

        def dfs(target):

            if target == 0:
                return 0
            
            if target in memo:
                return memo[target]

            res = float('inf')
            for i in range(1, target+1):
                if i*i <= target:
                    res = min(res, dfs(target - (i*i)))
                else:
                    break

            memo[target] = 1 + res       
            return memo[target]

        return dfs(n)
