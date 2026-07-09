class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        maxi = -1
        for elem in piles:
            if elem > maxi:
                maxi = elem
        
        s, e = 1, maxi
        ans = maxi
        while s <= e:
            mid = (s+e)//2
            time = 0
            for elem in piles:
                time += (elem + mid - 1)//mid
            if time > h:
                s = mid + 1
            elif time <= h:             ## IMP less than and equal condition is together
                ans = min(ans, mid)
                e = mid - 1
        return ans

