class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        n = len(intervals)
        intervals.sort()
        ans = []

        for i in range(1, n):
            if intervals[i][0] > intervals[i-1][1]:
                ans.append(intervals[i-1])
            else:
                intervals[i][0] = min(intervals[i][0], intervals[i-1][0])
                intervals[i][1] = max(intervals[i][1], intervals[i-1][1])
        ans.append(intervals[-1])
        return ans