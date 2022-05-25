class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt = 0
        for row in grid:
            l = 0
            r = len(row)-1
            while r > l+1:
                mid = (l+r)//2
                if row[mid] >= 0:
                    l = mid
                else:
                    r = mid
            if row[l] < 0:
                cnt += (len(row)-l)
            elif row[r] < 0:
                cnt += len(row)-r
        return cnt