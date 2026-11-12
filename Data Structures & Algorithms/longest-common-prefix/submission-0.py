class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(0, len(strs[0])):
            ch = strs[0][i]
            for j in range(1, len(strs)):
                if i < len(strs[j]):
                    if strs[j][i] == ch:
                        continue
                    else:
                        return strs[0][:i]   
                else:
                    return strs[0][:i]
                
        return strs[0]