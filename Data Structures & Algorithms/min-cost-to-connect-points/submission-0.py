class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        N = len(points)

        adj = {i: [] for i in range(N)}  # i : list of [cost, node]

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prim's
        ans = 0
        visited = set()
        min_heap = []  
        heapq.heappush(min_heap, (0, 0))

        while len(visited) < N:
            cost, point = heapq.heappop(min_heap)
            
            if point in visited:
                continue
            
            ans += cost
            visited.add(point)
            
            for nbrCost, nbr in adj[point]:
                if nbr not in visited:
                    heapq.heappush(min_heap, (nbrCost, nbr))

        return ans
        