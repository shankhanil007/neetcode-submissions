class Solution:
    def countSubstrings(self, s: str) -> int:
        
        ### IMPORTANT: can do using O(N^2) and O(1) SC
        
        self.maxLen = 1
        self.start = 0
        ans = 0

        def checkPalindrome(l, r):
            count = 0

            while l>=0 and r<n and s[l] == s[r]:
                count += 1
                length = r - l + 1
                if length > self.maxLen:
                    self.maxLen = length
                    self.start = l
                l -= 1
                r += 1
            return count

        n = len(s)
        for i in range(n):
            l, r = i, i
            ans += checkPalindrome(l, r)
            l, r = i, i+1
            ans += checkPalindrome(l, r)
        
        return ans