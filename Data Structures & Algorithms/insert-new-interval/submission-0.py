class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        ans = []
        last = len(intervals)

        for idx, elem in enumerate(intervals):
            if elem[1] < newInterval[0]:
                ans.append(elem)

            elif elem[0] > newInterval[1]:
                last = idx
                break

            else:
                minVal = min(elem[0], newInterval[0])
                maxVal = max(elem[1], newInterval[1])
                newInterval = [minVal, maxVal]

        ans.append(newInterval)
        for i in range(last, len(intervals)):
            ans.append(intervals[i])
        return ans
            