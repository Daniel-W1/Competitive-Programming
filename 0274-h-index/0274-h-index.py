class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        h_index = 0
        
        for idx, cite in enumerate(citations):
            pappers = idx + 1
            
            if cite < pappers:
                return idx
        
        return len(citations)
                
        