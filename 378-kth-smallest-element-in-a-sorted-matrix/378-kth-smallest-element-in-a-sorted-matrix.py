class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        maxheap = []
        for row in matrix:
            for val in row:
                if len(maxheap) < k:
                    heapq.heappush(maxheap, -val)
                else:
                    heapq.heappushpop(maxheap, -val)
        return -maxheap[0]