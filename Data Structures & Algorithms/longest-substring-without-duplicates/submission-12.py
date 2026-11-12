class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hmap = {}
        maxi = 0
        i, j = 0, 0
        while j < len(s):
            if s[j] in hmap.keys():
                i = max(hmap[s[j]] + 1, i)
            length = j-i+1
            maxi = max(length, maxi)
            hmap[s[j]] = j
            j += 1
        return maxi
