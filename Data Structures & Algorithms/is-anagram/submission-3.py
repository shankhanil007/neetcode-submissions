class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        ## Use two hmaps to store the count of the characters 
        ## of the strings and compare them
        
        if len(s) != len(t):
            return False

        hmapS, hmapT = {}, {}

        for i in range(0, len(s)):
            hmapS[s[i]] = hmapS.get(s[i], 0) + 1
            hmapT[t[i]] = hmapT.get(t[i], 0) + 1

        return hmapS == hmapT

        # Time complexity:  O(n+m) 
        # Space complexity:  O(1) since we have at most 26 different characters.
        
        
    ############################################################

    
        # if len(s) != len(t):
        #     return False

        # return sorted(s) == sorted(t)

        # Time complexity: O(nlogn+mlogm) 
        # Space complexity:  O(n+m) for Timsort


        
        