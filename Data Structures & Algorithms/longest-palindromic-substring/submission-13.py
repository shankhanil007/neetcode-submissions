class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        self.ans = ""
        self.maxLen = 0

        def helper(i, j): 
            maxLen = 0
            start = -1
            while i>=0 and j<n and s[i] == s[j]:
                length = j - i + 1
                if length > self.maxLen:
                    self.maxLen = length
                    self.ans = s[i:i+length]
                i -= 1
                j += 1
            return 

        
        for itr in range(n):
            helper(itr, itr)
            helper(itr, itr+1)
        
        return self.ans


            
