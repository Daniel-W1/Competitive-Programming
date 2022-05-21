class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = nums
        self.min_heap = self.arr[:k]
        self.cap = k
        heapq.heapify(self.min_heap)
        for val in self.arr[k:]:
            heapq.heappushpop(self.min_heap, val)
    def add(self, val: int) -> int:
        if len(self.min_heap)== self.cap:
            heapq.heappushpop(self.min_heap, val)
        else:
            heapq.heappush(self.min_heap, val)
        return self.min_heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)