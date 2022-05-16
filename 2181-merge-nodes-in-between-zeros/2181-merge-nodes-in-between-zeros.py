# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = newhead = ListNode()
        current = head
        while current:
            if current.val == 0 and not current.next: return dummy.next
            cursum = 0
            current = current.next
            while current and current.val != 0:
                cursum += current.val
                current = current.next
            newhead.next = ListNode(cursum)
            newhead = newhead.next
                
                
            