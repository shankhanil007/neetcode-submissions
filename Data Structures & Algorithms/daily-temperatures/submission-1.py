class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for j, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                last = stack.pop()
                i = last[1]
                ans[i] = j - i
            stack.append((temp, j))
        return ans

