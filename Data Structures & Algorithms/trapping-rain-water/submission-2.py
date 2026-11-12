class Solution:
    def trap(self, height: List[int]) -> int:
        
        # n = len(height)
        # left = [0] * n
        # right = [0] * n

        # curr_max = 0
        # for idx in range(n):
        #     curr_max = max(curr_max, height[idx])
        #     left[idx] = [curr_max, idx]
        
        # curr_max = 0
        # for idx in range(n-1, -1, -1):
        #     curr_max = max(curr_max, height[idx])
        #     right[idx] = [curr_max, idx]

        # ans = 0
        # for idx in range(n):
        #     width = right[idx][1] - left[idx][1] + 1
        #     top = min(left[idx][0], right[idx][0]) - height[idx]
        #     ans += (top * width)

        # return ans

        n = len(height)
        l, r = 1, n-2
        lmax, rmax = height[0], height[n-1]
        ans = 0

        while l <= r:
            if lmax <= rmax:
                water = lmax - height[l]
                if water > 0:
                    ans += water
                lmax = max(lmax, height[l])
                l += 1
            else:
                water = rmax - height[r]
                if water > 0:
                    ans += water
                rmax = max(rmax, height[r])
                r -= 1
        
        return ans







