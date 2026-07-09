class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxi = 0
        l = 0
        hmap = {} ### store the last seen idx of the char
        
        for idx, ch in enumerate(s):
            if ch in hmap.keys() and hmap[ch]>=l: ### VIMP if the char occur and the last idx of the char is in the current window
                l = hmap[ch] + 1
            hmap[ch] = idx
            maxi = max(idx-l+1,maxi)
        return maxi