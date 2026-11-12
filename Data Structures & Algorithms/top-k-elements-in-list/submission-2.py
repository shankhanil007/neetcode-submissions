class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num,0) + 1
        
        freq = [[] for _ in range(len(nums) + 1)]    ### Python list comprehension example
        for num, count in hmap.items():
            freq[count].append(num)

        ans = []
        for itr in range(len(freq)-1, -1, -1):   ### Python reverse loop
            if freq[itr] and k>0:
                while k!=0 and freq[itr]:
                    ans.append(freq[itr][-1])
                    freq[itr].pop()
                    k -= 1
        return ans
        