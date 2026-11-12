class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # hmap = {}
        # for i in range(0, len(nums)):
        #     rem = target - nums[i]
        #     if rem in hmap:
        #         return [min(i, hmap[rem]), max(i, hmap[rem])]
        #     hmap[nums[i]] = i
                

        
        #################### TWO PASSES ######################

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
                return [min(i, hmap[rem]), max(i, hmap[rem])]

        # Time complexity:  O(n) 
        # Space complexity:  O(n)


        ##########################################
        
        
        # 1. Create an ARRAY (IIIIMMMPPPP) NOT a Hashmap of [num, index]
        # 2. Iterate over array
        # 3. sum = arr[i][0] + arr[j][0]; 0th element for numbers
        # 4. If sum == target, then get the min, max of indexes; 1st element for idx
        
        # Time complexity:  O(nlogn) 
        # Space complexity:  O(n)
        

        # arr = []
        # for i in range(0, len(nums)):
        #     arr.append([nums[i], i])
        
        # arr.sort()            ################# IMP We Sort arr NOT nums
        # i, j = 0, len(nums)-1

        # while i<j:
        #     if arr[i][0] + arr[j][0] > target:
        #         j = j - 1
        #     elif arr[i][0] + arr[j][0] < target:
        #         i = i + 1
        #     else:
        #         return [min(arr[i][1], arr[j][1]), max(arr[i][1], arr[j][1])]



