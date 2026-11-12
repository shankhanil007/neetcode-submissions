class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_freq = [0]*26
        s2_freq = [0]*26
        l = 0

        for c in s1:
            idx = ord(c) - ord('a')
            s1_freq[idx] += 1

        for idx, c in enumerate(s2):
            if (idx - l + 1) > len(s1):
                index = ord(s2[l]) - ord('a')
                s2_freq[index] -= 1
                l += 1
            
            index = ord(s2[idx]) - ord('a')
            s2_freq[index] += 1

            if s2_freq == s1_freq:
                return True
        
        return False