class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [1] * len(nums) 

        for idx in range(1,len(nums)):
            ans[idx] = ans[idx-1] * nums[idx-1]

        postfix = nums[len(nums)-1]
        for idx in range(len(nums)-2, -1, -1):
            ans[idx] = ans[idx] * postfix
            postfix *= nums[idx]
            
        return ans

## Approach 1 - build prefix and suffix arrays and use them to create the final ans arrays
## Approach 2 - Use ans array in Pass 1 for prefix mul values. Re-use ans array in Pass 2 for suffix mul values