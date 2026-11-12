class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # hmap = defaultdict(int)
        # maxi, res = 0, 0
        # for num in nums:
        #     hmap[num] += 1
        #     if hmap[num] > maxi:
        #         maxi = hmap[num]
        #         res = num
        # return res

        # Space Complexity: O(N)


        ############## Bit Manipulation for Majority Element ##############

        bits = [0] * 32
        for num in nums:
            for i in range(0, 32):
                bits[i] += ((num >> i) & 1)

        res = 0
        for i in range(0, 32):
            if bits[i] > (len(nums) // 2):
                if i == 31:
                    res -= (1 << i)
                else:
                    res |= (1 << i)
            
        return res

        ############## Boyer-Moore Voting Algorithm ##############

        ## TO DO

