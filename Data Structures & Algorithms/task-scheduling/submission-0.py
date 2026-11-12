class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        maxHeap = []
        for k, v in freq.items():
            heapq.heappush(maxHeap, (-v, k))
        
        cycle = 0
        while maxHeap:
            temp = []
            for itr in range(0, n+1):
                if maxHeap or len(temp) > 0:
                    cycle += 1
                if maxHeap:
                    task = heapq.heappop(maxHeap)
                    new_freq = task[0]+1
                    if new_freq:
                        temp.append((new_freq, task[1]))
            for items in temp:
                heapq.heappush(maxHeap, (items[0], items[1]))
        return cycle
            
