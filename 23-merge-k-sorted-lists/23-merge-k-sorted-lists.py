# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
 
        while len(lists) > 1:
            new = []
            for i in range(0, len(lists), 2):
                dummy =tail = ListNode()
                if i + 1 < len(lists) : first, second = lists[i], lists[i+1]
                else:
                    new.append(lists[i])
                    break
                    
                while first and second:
                    if first.val < second.val:
                        tail.next, first = first, first.next
                    else:
                        tail.next, second = second, second.next
                    tail = tail.next

                tail.next = first or second
                new.append(dummy.next)
            lists = new
        return lists[0] if len(lists) > 0 else None