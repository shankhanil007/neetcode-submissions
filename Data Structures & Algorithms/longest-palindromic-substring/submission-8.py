class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        self.maxLen = 1
        self.start = 0

        def checkPalindrome(l, r):

            while l>=0 and r<n and s[l] == s[r]:
                length = r - l + 1
                if length > self.maxLen:
                    self.maxLen = length
                    self.start = l
                l -= 1
                r += 1

        n = len(s)
        for i in range(n):
            l, r = i, i
            checkPalindrome(l, r)
            l, r = i, i+1
            checkPalindrome(l, r)
        
        return s[self.start: self.start+self.maxLen]