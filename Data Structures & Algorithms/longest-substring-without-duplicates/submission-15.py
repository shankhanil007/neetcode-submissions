class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hmap = {}
        i, j = 0, 0
        ans = 0
        while j < len(s):
            while hmap.get(s[j], 0):
                hmap[s[i]] -= 1
                i += 1
            length = j - i + 1
            ans = max(ans, length)
            hmap[s[j]] = hmap.get(s[j], 0) + 1
            j += 1
        return ans
