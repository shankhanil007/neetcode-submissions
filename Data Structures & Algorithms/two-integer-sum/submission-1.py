class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        # 1. Create a hashmap of number and the last index of it
        # 2. Iterate over nums
        # 3. rem = target - nums[i]
        # 4. if rem exists in hashmap whose index != i; FOUND it

        hmap = {}
        for i in range(0, len(nums)):
            hmap[nums[i]] = i

        for i in range(0, len(nums)):
            rem = target - nums[i]
            if rem in hmap and hmap[rem] != i:
                return [i, hmap[rem]]


        ##########################################
        
        # 1. Create an ARRAY (IIIIMMMPPPP) NOT a Hashmap of [num, index]
        # 2. Iterate over array
        # 3. sum = arr[i][0] + arr[j][0]; 0th element for numbers
        # 4. If sum == target, then get the min, max of indexes; 1st element for idx
        
        # Time complexity:  O(nlogn) 
        # Space complexity:  O(n)
        