class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # A A A B B C C
        # 3, A
        # 2, B
        # 2, C
        # 1, D
        # 1, E

        
        # 1, B
        # 1, C
        # 1, E
        # 1, A

        # A B C D A 

        hmap = {}
        for task in tasks:
            hmap[task] = hmap.get(task, 0) + 1

        arr = []
        for task, freq in hmap.items():
            heapq.heappush(arr, (-freq, task))
        time = 0
        
        # time = 1
        
        # arr
        

        while arr:
            temp = []
            temp.append(arr[0]) # 2 X 2 Y
            heapq.heappop(arr) # 2 X will be popped
            time += 1 # 1
            cooldown = n
            if arr:
                while arr and cooldown:
                    temp.append(arr[0])
                    heapq.heappop(arr)
                    time += 1
                    cooldown -= 1
            for freq, task in temp:
                if freq < -1:
                    heapq.heappush(arr, (freq+1, task))
            if arr and cooldown:
                time += cooldown
        return time
                    








