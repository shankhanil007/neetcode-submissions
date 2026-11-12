class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    
        ans = []
        last_idx = len(intervals)

        for idx, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                ans.append(interval)

            elif interval[0] > newInterval[1]:
                last_idx = idx
                break   ### IMMMPPPP

            else:
                min_val = min(interval[0], newInterval[0])
                max_val = max(interval[1], newInterval[1])
                newInterval = [min_val, max_val]

        ans.append(newInterval)  ### IMMMPPP out the loop or else fails for [[1,3],[4,6]] and [2,5] becuz the final interval gets merge intervals (else block) does not have the append logic
        for i in range(last_idx, len(intervals)):
            ans.append(intervals[i])

        return ans
