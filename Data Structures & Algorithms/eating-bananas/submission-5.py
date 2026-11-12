class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        maxi = -1
        for pile in piles:
            maxi = max(maxi, pile)

        l, r = 1, maxi
        ans = maxi
        while l<=r:
            mid = (l+r)//2
            time = 0
            for pile in piles:
                if mid >= pile:
                    time += 1
                elif pile%mid == 0:
                    time += (pile)//mid
                else:
                    time += (pile)//mid + 1
            if time > h:
                l = mid + 1
            else:
                ans = min(ans, mid)
                r = mid - 1
                
        return ans
