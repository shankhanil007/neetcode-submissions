class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        i, j = 0, len(heights)-1
        maxi = 0
        while i < j:
            area = (j-i) * min(heights[i], heights[j])
            if heights[i] <= heights[j]:
                i += 1
            else: 
                j -= 1
            maxi = max(area, maxi)
        return maxi