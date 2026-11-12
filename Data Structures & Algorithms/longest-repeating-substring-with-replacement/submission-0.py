class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        hmap = {}
        max_len = 0
        max_freq = 0
        l = 0

        for idx, ch in enumerate(s):
            hmap[ch] = hmap.get(ch,0) + 1
            max_freq = max(max_freq, hmap[ch])
            while (idx - l + 1 - max_freq) > k:
                hmap[s[l]] -= 1
                l += 1
            max_len = max(max_len, idx - l + 1)
        return max_len