class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [-1]*k
        self.cursize = 0
        self.size = k
        self.read = 0
        self.write = 0

    def enQueue(self, value: int) -> bool:
        if self.cursize < self.size:
            self.q[self.write] = value
            self.write += 1
            self.write = (self.write) % self.size
            self.cursize += 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.cursize > 0:
            self.q[self.read] = -1
            self.read += 1
            self.read = (self.read) % self.size
            self.cursize -= 1
            return True
        return False

    def Front(self) -> int:
        return self.q[self.read]

    def Rear(self) -> int:
        if self.cursize > 0:
            return self.q[self.write-1] 
        return -1
    
    def isEmpty(self) -> bool:
        return self.cursize == 0

    def isFull(self) -> bool:
        return self.cursize == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
