class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 0, 10**15
        while left <= right:
            mid = (left + right)//2
            trips = 0
            for t in time:
                trips += mid//t
            if trips >= totalTrips:
                right = mid - 1
            else:
                left = mid + 1
                
        return right + 1
                