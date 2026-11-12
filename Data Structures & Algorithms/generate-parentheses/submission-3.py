class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ###### IIIIMMMPPP TODO: Solve using DP

        ans = []

        def helper(openB, closeB, currB):

            if openB == closeB and openB == n:
                ans.append(currB[:])
                return

            if openB < n:
                currB += "("
                openB += 1
                helper(openB, closeB, currB)
                currB = currB[:-1]
                openB -= 1
                
            if closeB < openB:
                currB += ")"
                closeB += 1
                helper(openB, closeB, currB)

        helper(0, 0, "")
        return ans
