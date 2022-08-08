class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        eqn_map = {}
        seen = set()
        max_cnt = 0
        
        if len(points) == 1:
            return 1
        for idx in range(len(points)):
            p1, p2 = points[idx]
            eqns = []
            for sec_idx in range(idx+1, len(points)):
                sp1, sp2 = points[sec_idx]
                slope = (sp2-p2)/(sp1-p1) if (sp1-p1) != 0 else float('inf')
               
                y_int = p2 - slope*p1 if slope != float('inf') else float('inf')
    
                if (slope, y_int) in seen: continue
                if (slope, y_int) not in eqn_map:
                    eqns.append((slope, y_int))
                eqn_map[slope, y_int] = eqn_map.get((slope, y_int), 1) + 1
                max_cnt = max(max_cnt, eqn_map[slope, y_int])
                
            for e in eqns:
                seen.add(e)
                
        return max_cnt
                
                
        