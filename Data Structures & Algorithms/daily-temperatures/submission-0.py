class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        output = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            while len(stack) != 0 and stack[-1][0] < temp:
                value = stack[-1]
                stack.pop()
                output[value[1]] = idx - value[1]
            stack.append((temp, idx))
        return output