class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        idx = bisect_right(intervals, newInterval)
        intervals.insert(idx, newInterval)
        
        # print(idx, intervals)
        
        start = intervals[0][0]
        prev = intervals[0][1]
        
        ans = []
        for idx in range(1, len(intervals)):
            if intervals[idx][0] > prev:
                ans.append([start, prev])
                start = intervals[idx][0]
                prev = intervals[idx][1]
            else:
                prev = max(prev, intervals[idx][1])
        
        ans.append([start, prev])
        
        return ans
        
            
       
        
            
            
                