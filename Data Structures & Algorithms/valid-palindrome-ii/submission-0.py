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
        
        i, j = 0, len(s) - 1
        counter = 0

        while i<j:
            while not s[i].isalnum():
                i += 1
            while not s[j].isalnum():
                j -= 1
            if s[i] != s[j]:
                if self.isPalindrome(s[i:j]) or self.isPalindrome(s[i+1:j+1]):
                    return True
                else:
                    return False
            i += 1
            j -= 1
        return True
                