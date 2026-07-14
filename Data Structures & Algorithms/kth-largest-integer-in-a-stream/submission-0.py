class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.my_heap = []
        for num in nums:
            if len(self.my_heap) < k:
                heapq.heappush(self.my_heap, num)
            else:
                if num > self.my_heap[0]:
                    heapq.heappop(self.my_heap)
                    heapq.heappush(self.my_heap, num)
        self.k = k

    def add(self, val: int) -> int:
        if len(self.my_heap) < self.k:
            heapq.heappush(self.my_heap, val)
        else:
            if val > self.my_heap[0]:
                heapq.heappop(self.my_heap)
                heapq.heappush(self.my_heap, val)
        return self.my_heap[0]

        