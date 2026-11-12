class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:









        ################ Approach 1 ################
        # 1. prefix = strs[0]
        # 2. Then compare str[0] with the corresponding strings and their letters
        # 3. If the letter mismath, replace prefix = strs[i]
        # 4. continue search
        # 5. Return prefix

        ###### COMMON Pitfall: strs=["abc","","abcd"]

        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break
                j = j + 1
            prefix = prefix[:j]

            
        return prefix


        # for i in range(0, len(strs[0])):
        #     ch = strs[0][i]
        #     for j in range(1, len(strs)):
        #         if i < len(strs[j]):
        #             if strs[j][i] == ch:
        #                 continue
        #             else:
        #                 return strs[0][:i]   
        #         else:
        #             return strs[0][:i]
                
        # return strs[0]