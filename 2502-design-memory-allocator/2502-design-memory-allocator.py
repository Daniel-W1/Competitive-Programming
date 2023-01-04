class Allocator:
    def __init__(self, n: int):
        self.ids = defaultdict(int)
        self.memory = [0]*n

    def allocate(self, size: int, mID: int) -> int:
        left = 0
        cnt = 0
        for right in range(len(self.memory)):
            if self.memory[right] not in self.ids:
                cnt += 1
            
            if right - left + 1 == size:
                if cnt == size: 
                    self.ids[mID] += size
                    
                    for idx in range(left, right + 1):
                        self.memory[idx] = mID
                        
                    return left
                
                if self.memory[left] not in self.ids:
                    cnt -= 1
                
                left += 1
        
        return -1
                

    def free(self, mID: int) -> int:
        val = self.ids[mID]
        del self.ids[mID]
        
        return val


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)