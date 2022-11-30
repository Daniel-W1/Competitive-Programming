class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        """
            1, 2, 3
            
            
                2
                
                1, 2, 3, 4
                [1, 0, 0, 0]
                   [1, 4]
        """
        heaters.sort()
        min_radius = 0
        
        for h in houses:
            idx = bisect_left(heaters, h)
            
            if idx == 0:
                min_radius = max(min_radius, heaters[0] - h)
            elif idx == len(heaters):
                min_radius = max(min_radius, h - heaters[-1])
            else:
                min_radius = max(min_radius, min(heaters[idx] - h, h - heaters[idx-1]))
        
        return min_radius