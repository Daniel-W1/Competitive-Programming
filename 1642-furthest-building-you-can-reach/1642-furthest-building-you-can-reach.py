class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minHeap = []
        for index in range(1, len(heights)):
            current_height = heights[index]
            prev_height = heights[index-1]
            
            if current_height > prev_height:
                heapq.heappush(minHeap, (current_height-prev_height))
                if len(minHeap) > ladders:
                    bricks -= heapq.heappop(minHeap) 
                if bricks < 0:
                    return index-1
        return len(heights)-1