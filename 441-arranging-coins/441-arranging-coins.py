class Solution:
    def arrangeCoins(self, n: int) -> int:
        # [1, 2, 3]
        l, h = 0, n
        formula = lambda n : n*(n+1)/2
        
        while l <= h:
            mid = (l+h)//2
            if formula(mid+1) == n:
                return mid + 1
            if formula(mid+1) > n and formula(mid) < n:
                return mid
            elif formula(mid) > n:
                h = mid - 1
            else:
                l = mid + 1
        return h
        print(l,h)
            