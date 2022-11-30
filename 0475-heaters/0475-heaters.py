class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        """
            1, 2, 3
            
            
                2
                
                1, 2, 3, 4
                [1, 0, 0, 0]
                   [1, 4]
        """
        houses.sort()
        heaters.sort()
        
        
        left, right = 0, 10**9
        answer = 0
        
        while left <= right:
            radius = (left + right)//2
            
            # now check the mid 
            arr = [0]*len(houses)
            for heater in heaters:
                l_end = heater - radius
                r_end = heater + radius
                
                l_idx = bisect_left(houses, l_end)
                r_idx = bisect_right(houses, r_end)
                
                # print(l_end, radius, heater)
                if l_idx < len(houses):
                    arr[l_idx] += 1
                if r_idx < len(houses):
                    arr[r_idx] -= 1
            
            
            arr = list(accumulate(arr))
            # print(arr, radius)
            # check for zero
            
            if 0 in arr:
                left = radius + 1
            else:
                answer = radius
                right = radius - 1
        
        return answer
    
                
                