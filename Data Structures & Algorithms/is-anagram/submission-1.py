class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hmapS, hmapT = {}, {}

        for i in range(0, len(s)):
            hmapS[s[i]] = hmapS.get(s[i], 0) + 1
            hmapT[t[i]] = hmapT.get(t[i], 0) + 1

        return hmapS == hmapT
        
        
        
        
        


        
        # Time complexity: O(nlogn+mlogm) 
        # Space complexity:  O(n+m) for Timsort

        # if len(s) != len(t):
        #     return False

        # return sorted(s) == sorted(t)


        
        