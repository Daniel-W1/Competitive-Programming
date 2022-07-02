class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        hc.sort()
        vc.sort()
        
        max_row,max_col = 0,0
        prev = 0
        for cut in hc:
            max_row = max(max_row,cut-prev)
            prev = cut
        max_row = max(max_row,h-prev)
        prev = 0
        for cut in vc:
            max_col = max(max_col,cut-prev)
            prev = cut
        max_col = max(max_col,w-prev)
        
        return (max_col*max_row)%(10**9+7)
            
        
            