class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        arr = [-s for s in stones]
        heapq.heapify(arr)

        while not len(arr) in [0, 1]:
            num1 = heapq.heappop(arr) * -1
            num2 = heapq.heappop(arr) * -1
            print(num1, num2)
            if num1 != num2:
                rem = num1 - num2
                print(rem)
                heapq.heappush(arr, rem * -1)

        return 0 if len(arr) == 0 else arr[0] * -1