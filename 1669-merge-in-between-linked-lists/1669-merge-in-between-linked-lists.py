# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = end = None
        
        current = list1
        idx = 1
        
        while current and current.next:
            if idx == a:
                start = current
                
            if idx == b + 1:
                end = current.next
                break
            
            current = current.next
            idx += 1
        
        # get the end of the middle list
        middle_l = list2
        start.next = middle_l
            
        while middle_l and middle_l.next:
            middle_l = middle_l.next
        
        middle_l.next = end
        
        return list1
        
        
        
                
                
                