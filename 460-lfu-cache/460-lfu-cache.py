# class Node:
#     def __init__(self, key, val):
#         self.key = key
#         self.val = val
#         self.freq = 1
#         self.prev = self.next = None

# class DLinkedList:
#     def __init__(self):
#         self._sentinel = Node(None, None) # dummy node
#         self._sentinel.next = self._sentinel.prev = self._sentinel
#         self._size = 0
    
#     def __len__(self):
#         return self._size
    
#     def append(self, node):
#         node.next = self._sentinel.next
#         node.prev = self._sentinel
#         node.next.prev = node
#         self._sentinel.next = node
#         self._size += 1
    
#     def pop(self, node=None):
#         if self._size == 0:
#             return
        
#         if not node:
#             node = self._sentinel.prev

#         node.prev.next = node.next
#         node.next.prev = node.prev
#         self._size -= 1
        
#         return node
        
# class LFUCache:
#     def __init__(self, capacity):
#         self._size = 0
#         self._capacity = capacity
        
#         self._node = dict() # key: Node
#         self._freq = collections.defaultdict(DLinkedList)
#         self._minfreq = 0
        
        
#     def _update(self, node):
#         freq = node.freq
        
#         self._freq[freq].pop(node)
#         if self._minfreq == freq and not self._freq[freq]:
#             self._minfreq += 1
        
#         node.freq += 1
#         freq = node.freq
#         self._freq[freq].append(node)
    
#     def get(self, key):
#         if key not in self._node:
#             return -1
        
#         node = self._node[key]
#         self._update(node)
#         return node.val

#     def put(self, key, value):
#         if self._capacity == 0:
#             return
        
#         if key in self._node:
#             node = self._node[key]
#             self._update(node)
#             node.val = value
#         else:
#             if self._size == self._capacity:
#                 node = self._freq[self._minfreq].pop()
#                 del self._node[node.key]
#                 self._size -= 1
                
#             node = Node(key, value)
#             self._node[key] = node
#             self._freq[1].append(node)
#             self._minfreq = 1
#             self._size += 1

from collections import defaultdict
from collections import OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = defaultdict(int) # key frequency
        self.freq = defaultdict(OrderedDict) # frequency OrderedDict
        self.min = 0
        
    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        
        f = self.d[key]
        val = self.freq[f][key]
        self.d[key] += 1
        del self.freq[f][key]
        self.freq[f + 1][key] = val
        
        if f == self.min and not self.freq[f]:
            self.min += 1
        
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.d:
            f = self.d[key]
            self.d[key] += 1
            del self.freq[f][key]
            self.freq[f + 1][key] = value
            if f == self.min and not self.freq[f]:
                self.min += 1
            return
        if len(self.d) == self.capacity:
            k, v = self.freq[self.min].popitem(last = False)
            del self.d[k]
        
        self.min = 1
        self.freq[1][key] = value
        self.d[key] = 1
        
        return

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)