class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = 0, len(citations)
        while left <= right:
            mid = (left + right)//2
            count = 0
            for cite in citations:
                if cite >= mid:
                    count += 1

            if count >= mid:
                left = mid + 1
            else:
                right = mid - 1
                
        return right 