class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # we need to choose some random max limit
        left, right = 1, 10**6
        def check(limit):
            temp = limit
            days = 0
            for weight in weights:
                if temp >= weight:
                    temp -= weight
                else:
                    days += 1
                    temp = limit
                    temp -= weight
                if temp < 0:
                    return float('inf')
            return days+1
        while left <= right:
            mid = (left+right)//2
            current_res = check(mid)
            
            if current_res <= days:
                right = mid - 1
            else:
                left = mid + 1
                
        return right + 1
                
                    
                