class MedianFinder:

    def __init__(self):
        self.mins = []
        self.maxs = []
    def addNum(self, num: int) -> None:
        heapq.heappush(self.mins, -num)
        if self.maxs and num > self.maxs[0]:
            heapq.heappush(self.maxs, -heapq.heappop(self.mins))
        if len(self.maxs) > len(self.mins)+1:
            max_min = heapq.heappop(self.maxs)
            heapq.heappush(self.mins, -max_min)
        if len(self.mins) > len(self.maxs)+1:
            min_max = heapq.heappop(self.mins)
            heapq.heappush(self.maxs, -min_max)
        
    def findMedian(self) -> float:
        if len(self.maxs) != len(self.mins):
            if len(self.maxs) > len(self.mins):
                return self.maxs[0]
            return -self.mins[0]
        return (-self.mins[0]+self.maxs[0])/2
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()