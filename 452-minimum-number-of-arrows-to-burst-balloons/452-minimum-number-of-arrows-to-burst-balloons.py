class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        start, end = points[0]
        cnt = 0
        
        for s, e in points:
            if end >= s:
                start = max(s, start)
                end = min(e, end)
            else:
                cnt += 1
                start = s
                end = e
        return cnt + 1
                
            
            