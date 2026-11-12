class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        window = len(s1)
        freq1 = [0] * 26
        for ch in s1:
            freq1[ord(ch)-ord('a')] += 1

        i, j = 0, 0
        freq2 = [0] * 26
        while j < len(s2):
            freq2[ord(s2[j])-ord('a')] += 1
            size = j - i + 1
            if size > window:
                freq2[ord(s2[i])-ord('a')] -= 1
                i += 1
            if freq1 == freq2:
                return True
            j += 1
        return False
            

