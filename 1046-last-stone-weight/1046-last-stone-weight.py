class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-val for val in stones]
        while len(stones) > 1:
            heapq.heapify(stones)
            max1 = -stones.pop(0)
            heapq.heapify(stones)
            max2 = -stones.pop(0)
            if max1 != max2:
                heapq.heappush(stones,-(max1-max2))
        return -stones[0] if stones else 0
        
        
        