class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hmap = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            hmap[tuple(count)].append(s)

        return list(hmap.values())

        # Time complexity:  O(m∗n) 
        # Space complexity: O(m∗n*26)


        #########################################################
        # IMPORTANT - you cannot use hmap[ASCII Count] because different chars
        # can combine to give the same count

        # hmap = defaultdict(list)

        # for s in strs:
        #     sortedS = ''.join(sorted(s))
        #     hmap[sortedS].append(s)

        # return list(hmap.values())

        # Time complexity:  O(m∗nlogn) 
        # Space complexity:  O(m∗n) ############# IMPORTANT Hash Map SC ############