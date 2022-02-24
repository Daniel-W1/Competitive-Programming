class Solution:
    def hIndex(self, citations: List[int]) -> int:
        the_max = len(citations)
        
        if len(citations)==1:
            if citations[0] == 0: return 0
            else: return 1
            
        for check in range(the_max, -1, -1):
            cnt = 0
            for val in citations[::-1]:
                if check <= val and cnt < check: 
                    cnt += 1
                if cnt == check:
                    return check
            
            
                
                
            
        