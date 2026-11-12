"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if len(intervals) == 0:
            return 0

        intervals.sort(key = lambda x: x.start)
        arr = []
        heapq.heappush(arr, intervals[0].end)
        ans = 1

        for i in range(1, len(intervals)):
            end = arr[0]

            if intervals[i].start >= end:
                heapq.heappop(arr)
            
            heapq.heappush(arr, intervals[i].end)
            ans = max(ans, len(arr))

        return ans

