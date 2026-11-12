class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxi = 0
        l, r = 0, -1
        hmap = {}

        for idx in range(0, len(s)):
            ch = s[idx]
            if hmap.get(ch) is None:
                r += 1
                maxi = max(maxi, r - l + 1)
                hmap[ch] = 1
            else:
                while hmap[ch] != 0:
                    hmap[s[l]] -= 1
                    l += 1
                r += 1
                maxi = max(maxi, r - l + 1)
                hmap[ch] = 1
        return maxi

