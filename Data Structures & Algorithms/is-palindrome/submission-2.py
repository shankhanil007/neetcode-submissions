class Solution:

    def checkIsAlphaNum(self, ch):
        if (ord(ch) >= 97 and ord(ch) <= 122) or (ord(ch) >= 48 and ord(ch) <= 57):
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        i, j = 0, len(s)-1
        while(i<j):
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
            