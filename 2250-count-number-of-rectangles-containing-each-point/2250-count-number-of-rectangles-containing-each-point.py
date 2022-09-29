class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        rectangles.sort()
        height_map = defaultdict(list)
        
        for w, h in rectangles:
            height_map[h].append(w)
        
        ans = []
        
        # print(height_map)
        for point in points:
            w, h = point
            cnt = 0
            # print('current',h)
            for height in height_map:
                if height >= h:
                    nums = height_map[height]
                    pos = bisect_left(nums, w)
                    cnt += len(nums)-pos
            ans.append(cnt)
            
        return ans
                    
                    
                    
        
            
            