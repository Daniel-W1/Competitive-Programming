class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 0, x//2
        if x == 1:
            return 1
        while l <= h:
            mid = (l+h)//2
            if mid**2 == x:
                return mid
            elif mid**2 > x:
                h = mid - 1
            else:
                l = mid + 1
        return mid if mid**2 <= x else mid-1
        