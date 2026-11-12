from _heapq import heapify
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        while k > 0:
            top = heapq.heappop(nums) * -1
            k -= 1
        return top