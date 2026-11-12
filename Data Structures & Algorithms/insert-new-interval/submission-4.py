class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    
        ans = []
        last_idx = len(intervals)

        for idx, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                ans.append(interval)

            elif interval[0] > newInterval[1]:
                last_idx = idx
                break

            else:
                min_val = min(interval[0], newInterval[0])
                max_val = max(interval[1], newInterval[1])
                newInterval = [min_val, max_val]

        ans.append(newInterval)
        for i in range(last_idx, len(intervals)):
            ans.append(intervals[i])

        return ans
