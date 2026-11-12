class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        self.count = 0
        

        def helper(i, j): 
            maxLen = 0
            start = -1
            while i>=0 and j<n and s[i] == s[j]:
                length = j - i + 1
                self.count += 1
                i -= 1
                j += 1
            return 

        
        for itr in range(n):
            helper(itr, itr)
            helper(itr, itr+1)
        
        return self.count
