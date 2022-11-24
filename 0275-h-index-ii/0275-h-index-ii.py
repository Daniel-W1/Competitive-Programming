class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        left, right = 0, len(citations)-1
        h_index = 0
        
        while left <= right:
            
            mid = (left + right)//2
            
            pappers = len(citations) - mid
            
            if citations[mid] >= pappers:
                h_index = pappers
                right = mid - 1
            else:
                left = mid + 1
        
        return h_index