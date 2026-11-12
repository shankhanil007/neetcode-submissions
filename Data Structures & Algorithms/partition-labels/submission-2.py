class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        hmap = {}
        for idx, ch in enumerate(s):
            hmap[ch] = idx

        ans = []
        curr = ""
        max_range = -1

        for idx, ch in enumerate(s):
            last_pos = hmap[ch]
            max_range = max(max_range, last_pos)
            curr += ch
            if idx == max_range:
                ans.append(len(curr))
                curr = ""
        
        return ans
                



        