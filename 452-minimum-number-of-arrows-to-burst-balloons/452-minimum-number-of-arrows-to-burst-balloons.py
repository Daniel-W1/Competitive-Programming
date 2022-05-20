class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        prev = points[0]
        removed = 0
        for point in points[1:]:
            if prev[1] >= point[0]:
                removed += 1
                if prev[1] > point[1]:
                    prev = point
            else:
                prev = point
        return len(points)-removed
            
            
        