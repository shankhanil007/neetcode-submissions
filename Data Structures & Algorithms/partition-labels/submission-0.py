class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        hmap = {}
        for idx, ch in enumerate(s):
            hmap[ch] = idx

        l, r = 0, 0
        ans = []

        for idx, ch in enumerate(s):
            if idx > r:
                window = r-l+1
                ans.append(window)
                l = idx
                r = hmap[ch]
                # if idx == len(s) - 1:
                
            else:
                r = max(r, hmap[ch])
        window = r-l+1
        ans.append(window)
        return ans

            
