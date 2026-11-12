class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num,0) + 1
        
        freq = [[] for _ in range(len(nums) + 1)]

        print(freq)

        for num, count in hmap.items():
            print(num, count, freq[count])
            freq[count].append(num)
            print(num, count, freq[count])
            print(freq)

        ans = []
        for itr in range(len(freq)-1, -1, -1):
            if freq[itr]:
                while k!=0 and freq[itr]:
                    ans.append(freq[itr][-1])
                    freq[itr].pop()
                    k -= 1
        return ans
        