class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        arr = []
        for elem in nums:
            if len(arr) < k:
                heapq.heappush(arr, elem)
            else:
                if elem > arr[0]:
                    heapq.heappop(arr)
                    heapq.heappush(arr, elem)
        return arr[0]