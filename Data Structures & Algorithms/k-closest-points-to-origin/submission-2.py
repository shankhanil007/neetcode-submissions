class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        for idx, point in enumerate(points):
            x = point[0]
            y = point[1]
            dis = (x*x) + (y*y)
            points[idx] = (dis, (x,y))

        heapq.heapify(points)            
        ans = []
        while k != 0:
            ans.append(heapq.heappop(points)[1])
            k -= 1

        return ans