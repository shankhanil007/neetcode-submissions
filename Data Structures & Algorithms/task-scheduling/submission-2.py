class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        maxHeap = []
        for k, v in freq.items():
            heapq.heappush(maxHeap, -v)

        cycles = 0
        while maxHeap:
            curr = heapq.heappop(maxHeap)
            cycles += 1
            temp = []
            for i in range(n):
                if maxHeap:
                    temp.append(heapq.heappop(maxHeap))
                    cycles += 1
            if curr != -1:  ### end of heap imp condition
                cycles += (n - len(temp))
                heapq.heappush(maxHeap, curr+1)
            for elem in temp:
                if elem != -1:  ### end of heap imp condition
                    heapq.heappush(maxHeap, elem+1)

        return cycles
            

            