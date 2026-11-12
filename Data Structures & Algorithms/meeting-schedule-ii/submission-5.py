"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if not intervals:
            return 0

        intervals.sort(key = lambda x: x.start)
        arr = []
        ans = -float('inf')

        for elem in intervals:
            if not arr:
                heapq.heappush(arr, elem.end)
            else:
                if elem.start >= arr[0]:
                    heapq.heappop(arr)
                heapq.heappush(arr, elem.end)
            ans = max(ans, len(arr))
        
        return ans
