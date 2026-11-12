class Solution:
    def mySqrt(self, x: int) -> int:

        # If m * m < x, m is a valid candidate. 
        # Store it in res and search for a larger value by setting l = m + 1

        l, r = 0, x
        res = 0
        while l<=r:
            mid = (l+r)//2
            if mid*mid > x:
                r = mid - 1
            elif mid*mid < x:
                res = mid
                l = mid + 1
            else:
                return mid
        return res