class Solution:

    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i<j:
            while not s[i].isalnum():
                i += 1
            while not s[j].isalnum():
                j -= 1
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(l, r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l, r = l+1, r-1
            return True


        i, j = 0, len(s) - 1

        while i<j:
            if s[i] != s[j]:
                if isPalindrome(i,j-1) or isPalindrome(i+1,j):
                    return True
                else:
                    return False
            i, j = i+1, j-1
        return True
                