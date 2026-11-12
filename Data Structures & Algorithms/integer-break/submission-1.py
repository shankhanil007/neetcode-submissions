class Solution:
    def integerBreak(self, n: int) -> int:
        
        memo = {}
        def helper(root, parent):
            
            if root in memo:
                return memo[root]

            maxi = -1
            if parent != -1:
                maxi = root
            
            for i in range(1, root//2+1):
                val1 = i
                val2 = root - val1
                maxi = max(maxi, val1 * val2)

                if val1 != 1:
                    maxi = max(maxi, val2 * helper(val1, 0))
                    
                if val2 != 1:
                    maxi = max(maxi, val1 * helper(val2, 0))
            
            memo[root] = maxi
            return memo[root]

        return helper(n, -1)


        