class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = 0, len(citations)-1
        n = len(citations)
        
        while left <= right:
            mid = (left + right)//2
            
            if citations[mid] == n-mid:
                return n-mid
            if citations[mid] > n- mid:
                right = mid - 1
            else:
                left = mid + 1

        return n - left