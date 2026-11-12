class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        hmap = {}
        for idx, num in enumerate(numbers):
            rem = target - num
            if rem in hmap:
                return [hmap[rem], idx+1]
            hmap[num] = idx+1