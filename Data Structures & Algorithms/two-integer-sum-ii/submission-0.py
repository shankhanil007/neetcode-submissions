class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, h = 0, len(numbers)-1
        while l < h:
            result = numbers[l] + numbers[h]
            if result == target:
                return [l+1, h+1]
            elif result < target:
                l += 1
            else:
                h -= 1