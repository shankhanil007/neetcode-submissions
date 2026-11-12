class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxi = -1
        for height in piles:
            maxi = max(height, maxi)
        
        high = maxi
        low = 1
        ans = maxi

        while low <= high:
            mid = (low+high)//2
            time = 0
            for height in piles:
                time += math.ceil(height/mid)
            if time > h:
                low = mid + 1
            else:
                ans = min(mid, ans)
                high = mid -1
        return ans


