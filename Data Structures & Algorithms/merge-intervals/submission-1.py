class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        temp = intervals[0]
        ans = []

        for i in range(1, len(intervals)):
            if intervals[i][0] > temp[1]:
                ans.append(temp)
                temp = intervals[i]
            else:
                minVal = min(temp[0], intervals[i][0])
                maxVal = max(temp[1], intervals[i][1])
                temp = [minVal, maxVal] 
        ans.append(temp) #### IMMMPPP
        return ans