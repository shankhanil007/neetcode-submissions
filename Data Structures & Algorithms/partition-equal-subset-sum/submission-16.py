class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2:
            return False

        n = len(nums)
        target = sum(nums)//2
        prev = [False] * (target+1)
        curr = [False] * (target+1)

        prev[0], curr[0] = True, True

        for i in range(1, n):
            for j in range(1, target+1):
                not_take = prev[j]
                take = False
                if nums[i] <= j:
                    take = prev[j - nums[i]] ### Till index i can you make the target
                curr[j] = take or not_take
            prev = curr[:]

        return prev[target]


