class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k
        for num in nums:
            if len(self.minHeap) < k:
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappushpop(self.minHeap, num)

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        else:
            heapq.heappushpop(self.minHeap, val)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)