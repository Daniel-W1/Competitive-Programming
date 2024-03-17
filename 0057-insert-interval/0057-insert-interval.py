class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        pos = len(intervals)
        
        for idx, (start, end) in enumerate(intervals):
            if start >= newInterval[0]:
                pos = idx
                break
            elif end >= newInterval[0]:
                pos = idx + 1
                break
            
        
        intervals.insert(pos, newInterval)
        merged_intervals = []
        
        for start,end in intervals:
            if not merged_intervals:
                merged_intervals.append([start, end])
            elif merged_intervals[-1][1] >= start:
                merged_intervals[-1][1] = max(end, merged_intervals[-1][1])
            else:
                merged_intervals.append([start, end])
        
        return merged_intervals
        