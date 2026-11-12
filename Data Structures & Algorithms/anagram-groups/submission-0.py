class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = {}

        for st in strs:
            sorted_st = "".join(sorted(st))
            hmap.setdefault(sorted_st, []).append(st)

        ans = []
        for val in hmap.values():
            ans.append(val)
        
        return ans
