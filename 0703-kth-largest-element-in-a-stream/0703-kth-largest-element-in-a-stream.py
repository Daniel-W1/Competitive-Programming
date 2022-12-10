class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        
        for num in nums:
            if len(self.heap) < self.k:
                heappush(self.heap, num)
            else:
                heappushpop(self.heap, num)
        

    def add(self, num: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, num)
        else:
            heappushpop(self.heap, num)
        
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)