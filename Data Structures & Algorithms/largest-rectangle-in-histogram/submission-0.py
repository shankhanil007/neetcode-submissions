class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        ans = 0

        for idx, height in enumerate(heights):
            if not stack:
                stack.append((idx, height))
            else:
                last_idx = float('inf')
                while stack and stack[-1][1] > height:
                    last_idx = min(last_idx, stack[-1][0])
                    area = (idx - stack[-1][0]) * stack[-1][1]
                    stack.pop()
                    ans = max(ans, area)
                if last_idx != float('inf'):
                    stack.append((last_idx, height))
                else:
                    stack.append((idx, height))
        
        end = len(heights) 
        while stack:
            idx, value = stack.pop()
            area = (end-idx) * value
            ans = max(ans, area)

        return ans
