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
        ans = -1

        for idx, interval in enumerate(intervals):
            if arr and interval.start >= arr[0]:
                heapq.heappop(arr)
            heapq.heappush(arr, interval.end)
            
            ans = max(ans, len(arr))

        return ans


        