class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        freq1 = [0] * 26
        freq2 = [0] * 26

        for ch in s1:
            idx = ord(ch) - ord('a')
            freq1[idx] += 1

        left, right = 0,0
        while right < len(s2):

            
            
            if (right-left+1) > len(s1):
                idx = ord(s2[left]) - ord('a')
                freq2[idx] -= 1
                left += 1

            idx = ord(s2[right]) - ord('a')
            freq2[idx] += 1

            if (right-left+1) == len(s1):
                if freq1 == freq2:
                    return True
            
            right += 1
            
        return False
