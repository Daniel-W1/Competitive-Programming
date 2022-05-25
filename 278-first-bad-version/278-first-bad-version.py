# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        while l+1 < r:
            mid = (l + r)//2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid
        return l if isBadVersion(l) else r
                
            
        
        