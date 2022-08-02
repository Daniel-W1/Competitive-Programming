class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-val for val in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            first_max = -heapq.heappop(maxHeap)
            second_max = -heapq.heappop(maxHeap)
            
            if first_max != second_max:
                heapq.heappush(maxHeap, -(first_max - second_max))
        return -maxHeap[0] if maxHeap else 0
        
        
        
            
            
           
                