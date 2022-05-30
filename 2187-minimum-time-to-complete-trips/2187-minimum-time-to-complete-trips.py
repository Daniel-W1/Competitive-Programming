class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l = 0
        tail = totalTrips*min(time)
        while l < tail:
            mid = (l+tail)//2
            cnt = 0
            for val in time:
                cnt += (mid//val)
            if cnt >= totalTrips:
                tail = mid
            else:
                l = mid + 1
        return l