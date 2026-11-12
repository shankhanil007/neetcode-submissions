class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i = 0
        res = [] ### Use array instead of string

        while i < len(word1) or i < len(word2):
            # res += word1[i] + word2[j]    ### SLOWER Python cannot just modify your existing res string. 
            ##                                          Instead, it is forced to create a completely brand-new string copy in memory every single time the loop runs.
            if i < len(word1):
                res.append(word1[i])
            if i < len(word2):
                res.append(word2[i])
            i += 1
        
        return "".join(res)
