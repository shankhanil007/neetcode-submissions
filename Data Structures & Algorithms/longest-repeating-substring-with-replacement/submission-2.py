class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}
        max_freq = 0
        i = 0
        maxi = 0
        for j, ch in enumerate(s):
            hmap[ch] = hmap.get(ch,0) + 1
            max_freq = max(hmap[ch], max_freq)
            
            while ((j-i+1) - max_freq) > k:
                hmap[s[i]] -= 1
                i += 1

            maxi = max((j-i+1), maxi)
        return maxi

            
            

