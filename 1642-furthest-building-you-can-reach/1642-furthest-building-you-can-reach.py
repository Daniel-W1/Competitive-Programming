from heapq import heapify, heappop, heappush
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minHeap = []
        heapify(minHeap)
        for i in range(len(heights)-1):
            diff = heights[i+1]-heights[i]
            if diff > 0:
                heappush(minHeap, diff)
            if len(minHeap) > ladders:
                bricks -= heappop(minHeap)
            if bricks < 0:
                return i
        return len(heights)-1
        