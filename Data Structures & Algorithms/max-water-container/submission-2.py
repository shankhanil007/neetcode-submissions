class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, h = 0, len(heights)-1
        maxi = -1
        while l < h:
            water = (h-l) * min(heights[l],heights[h])
            maxi = max(water, maxi)
            if heights[l] < heights[h]:
                l += 1
            else:
                h -= 1
        return maxi

#########
# When pointer moves inward, the width shrinks.
# Bigger area in the future is possible only when height increases 
#########