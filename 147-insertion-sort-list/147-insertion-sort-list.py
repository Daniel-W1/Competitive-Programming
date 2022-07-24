# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first,prev = head, head
        start = first.next
        
        while start:
            if start.val < prev.val:
                # do the insert logic
                temp = start
                the_next = start.next
                prev.next = prev.next.next
                if first.val > temp.val:
                    temp.next = first
                    head = temp
                    first = head
                else:
                    prevn = None
                    while first:
                        if first.val > temp.val:
                            prevn.next = temp
                            temp.next = first
                            break
                        else:
                            prevn = first
                        first = first.next
                    first = head
                start = the_next
            else:
                prev = start
                start = start.next
        return head