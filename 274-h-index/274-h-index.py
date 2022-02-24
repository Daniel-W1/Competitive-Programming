class Solution:
    def hIndex(self, citations: List[int]) -> int:
        the_max = len(citations)
        citations= sorted(citations, reverse = True)
        if len(citations)==1:
            if citations[0] == 0: return 0
            else: return 1
            
        for check in range(the_max, -1, -1):
            cnt = 0
            for val in citations:
                if check <= val and cnt < check: 
                    cnt += 1
                else:
                    if cnt == check:
                        return check
                    break
                if cnt == check:
                    return check
            
            
                
                
            
        