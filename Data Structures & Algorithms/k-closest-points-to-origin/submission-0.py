class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distance = []

        for point in points:
            x = point[0]
            y = point[1]
            dis = math.sqrt((x*x) + (y*y))
            heapq.heappush(distance,(dis, (x,y)))
        
        print(distance)

        ans = []
        while k != 0:
            ans.append(heapq.heappop(distance)[1])
            k -= 1

        return ans
