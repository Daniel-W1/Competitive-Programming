class RandomizedCollection:

    def __init__(self):
        self.count = defaultdict(set)
        self.alist = []

    def insert(self, val: int) -> bool:
        self.alist.append(val)
        self.count[val].add(len(self.alist) - 1)
        
        return len(self.count[val]) == 1
            
    
    def remove(self, val: int) -> bool:
        if val not in self.count:
            return False
        
        inds = self.count[val]
        for idx in inds:
            index = idx
            break
        
        inds.remove(index)
        if not self.count[val]:
            del self.count[val]
            
        if len(self.alist) > 1 and index != len(self.alist)-1:
            self.alist[index] = self.alist[-1]
            val = self.alist[-1]
            self.count[val].remove(len(self.alist)-1)
            self.count[val].add(index)
            
        self.alist.pop()
        return True

    def getRandom(self) -> int:
        randidx = randint(0, len(self.alist)-1)
        return self.alist[randidx]
        
        
# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()