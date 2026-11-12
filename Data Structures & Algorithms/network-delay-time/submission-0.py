class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = {i: [] for i in range(1, n+1)}
        for u, v, weight in times:
            adj[u].append((v, weight))

        arr = []
        visited = set()
        ans = 0

        heapq.heappush(arr, (0, k))

        while arr:
            time, node = heapq.heappop(arr)

            if node in visited:
                continue
            
            visited.add(node)
            ans = max(ans, time)

            for nbr, weight in adj[node]:
                if nbr not in visited:
                    heapq.heappush(arr, (time+weight, nbr))
                    
        if len(visited) != n:
            return -1
        return ans