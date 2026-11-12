class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        hmap = {}
        maxFreq = 0
        l, r = 0, 0
        ans = 0

        while r < len(s):
            ch = s[r]
            hmap[ch] = hmap.get(ch, 0) + 1
            maxFreq = max(maxFreq, hmap[ch])
            
            while (r-l+1) - maxFreq > k:
                hmap[s[l]] -= 1
                l += 1

            window = (r-l+1) 
            ans = max(ans, window)
            r += 1

        return ans

