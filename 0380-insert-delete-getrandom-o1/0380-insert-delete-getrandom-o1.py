class RandomizedSet:

    def __init__(self):
        self.elements = {}
        self.element_list = []
        self.idx = 0

    def insert(self, val: int) -> bool:
        if val in self.elements: return False
        self.elements[val] = self.idx
        self.idx += 1
        
        self.element_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.elements: return False
        # swap it with the last element
        
        last_element = self.element_list[-1]
        del_idx = self.elements[val]
        self.elements[last_element] = del_idx
        del self.elements[val]
        
        self.element_list[-1], self.element_list[del_idx] = self.element_list[del_idx], self.element_list[-1]
        self.element_list.pop()
        
        self.idx -= 1
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.element_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()