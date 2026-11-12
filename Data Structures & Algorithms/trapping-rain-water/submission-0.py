class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        left = [0] * n
        right = [0] * n

        curr_max = 0
        for idx in range(n):
            curr_max = max(curr_max, height[idx])
            left[idx] = [curr_max, idx]
        
        curr_max = 0
        for idx in range(n-1, -1, -1):
            curr_max = max(curr_max, height[idx])
            right[idx] = [curr_max, idx]


        ans = 0
        for idx in range(n):
            width = right[idx][1] - left[idx][1] + 1
            top = min(left[idx][0], right[idx][0]) - height[idx]
            ans += (top * width)

        return ans