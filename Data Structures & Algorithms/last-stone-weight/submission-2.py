class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            num1 = heapq.heappop(stones) * -1
            num2 = heapq.heappop(stones) * -1
            if num1 != num2:
                rem = abs(num1-num2)
                heapq.heappush(stones, -rem)
        
        return 0 if len(stones) == 0 else stones[0] * -1

