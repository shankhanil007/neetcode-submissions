class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:









        ################ Approach 1 ################
        # 1. prefix = strs[0]
        # 2. Then compare str[0] with the corresponding strings and their letters
        # 3. If the letter mismath, replace prefix = strs[i]
        # 4. continue search
        # 5. Return prefix

        ###### COMMON Pitfall: strs=["abc","","abcd"] or ["abcd", "cd"]

        # prefix = strs[0]
        # for i in range(1, len(strs)):
        #     j = 0
        #     while j < min(len(prefix), len(strs[i])):
        #         if prefix[j] != strs[i][j]:
        #             break
        #         j = j + 1
        #     prefix = prefix[:j]            
        # return prefix

        # Time complexity:  O(n∗m) 
        # Space complexity: O(m)
        # m = length of the longest string


        ################ Approach 2 ################

        for i in range(len(strs[0])):
            ch = strs[0][i]
            for s in strs:      ############################### IIIIIMPPPPPPPPPPPPPPPPP
                if i == len(s) or s[i] != ch:
                    return s[:i]
        return strs[0] ############################### IIIIIMPPPPPPPPPPPPPPPPP

        # Time complexity:  O(n*m) 
        # Space complexity: O(1) since we did not use extra space




