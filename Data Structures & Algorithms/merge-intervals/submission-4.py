class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        ans = []
        intervals.sort()
        temp = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] > temp[1]:
                ans.append(temp)
                temp = intervals[i]
            else:
                min_val = min(intervals[i][0], temp[0])
                max_val = max(intervals[i][1], temp[1])
                temp = [min_val, max_val]

        ans.append(temp)
        return ans