class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = -1
        for elem in piles:
            r = max(r, elem)

        ans = r

        while l<=r:
            mid = (l+r)//2
            time = 0
            for elem in piles:
                if elem <= mid:
                    time += 1
                else:
                    time += elem//mid if elem%mid == 0 else elem//mid + 1
            print(time)
            if time <= h:
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
            
            
            
        return ans


                
        