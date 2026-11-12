class Solution:
    
    def twoSum(self, nums, target, idx, ans):
        l, h = idx, len(nums)-1
        while l < h:
            result = nums[l] + nums[h]
            if result == target:
                ans.append([nums[l], nums[h], -target])
                l += 1
                h -= 1
                while l < h and nums[l] == nums[l-1]:
                    l += 1
                while l < h and nums[h] == nums[h+1]:
                    h -= 1
            elif result < target:
                l += 1
            else:
                h -= 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums.sort()  ## IMP two sum works on sorted array

        for idx, num in enumerate(nums):
            if num > 0:    ## IMP all remaining numbers are positive
                break

            if idx != 0 and num == nums[idx-1]:  ## IMP Skip duplicate values for the first number.
                continue

            l, h = idx + 1, len(nums)-1
            while l < h:
                threeSum = num + nums[l] + nums[h]
                if threeSum > 0:
                    h -= 1
                elif threeSum < 0: 
                    l += 1
                else:
                    ans.append([num, nums[l], nums[h]])
                    l += 1
                    h -= 1
                    while nums[l] == nums[l - 1] and l < h:
                        l += 1
        return ans


