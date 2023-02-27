# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nested = nestedList
        self.flattened = self.flatten(nestedList)
        self.pointer = 0
        
    
    def next(self) -> int:
        
        return self.flattened[self.pointer-1]
        # seems like am going to call the nestedList thing recursively when ever i find a list
        
    
    def hasNext(self) -> bool:
        if self.pointer < len(self.flattened):
            self.pointer += 1
            return True
        return False
    
    def flatten(self, arr):
        
        # print(type(arr), arr)
        
        res = []
        
        for _object in arr:
            if _object.isInteger():
                res.append(_object.getInteger())
            else:
                res.extend(self.flatten(_object.getList()))
        
        return res
                
        
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())