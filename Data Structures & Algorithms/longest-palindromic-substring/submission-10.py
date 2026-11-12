class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)

        def checkPallindrome(l, r):
            length = 0
            start = l
            while l>=0 and r<n and s[l] == s[r]:
                length = (r-l+1)
                start = l
                l-=1
                r+=1
            return start, length

        ans, start = 0, 0
        for i in range(n):
            srt, count = checkPallindrome(i, i)
            if count > ans:
                ans = count
                start = srt
            srt, count = checkPallindrome(i, i+1)
            if count > ans:
                ans = count
                start = srt
        return s[start:start+ans]


