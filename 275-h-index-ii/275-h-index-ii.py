class Solution:
    def hIndex(self, citations: List[int]) -> int:
        lo, hi = 0, len(citations)

        while lo < hi:
            mid = hi - (hi - lo) // 2
            if citations[-mid] >= mid:
                lo = mid
            else:
                hi = mid - 1
        return lo