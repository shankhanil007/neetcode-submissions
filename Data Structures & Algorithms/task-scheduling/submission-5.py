class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        hmap = {}
        for task in tasks:
            hmap[task] = hmap.get(task, 0) + 1

        arr = []
        for task, freq in hmap.items():
            heapq.heappush(arr, -freq)
        
        max_freq = -arr[0]
        idle_slots = (max_freq-1) * n
        heapq.heappop(arr)

        while arr:
            possible_slots = min(-arr[0], max_freq - 1)
            idle_slots -= possible_slots
            heapq.heappop(arr)

        if idle_slots <= 0:
            return len(tasks)
        else:
            return len(tasks) + idle_slots
