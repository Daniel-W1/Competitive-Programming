# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], l: int, r: int) -> Optional[ListNode]:
        dummynode = ListNode(0, head)
        leftprev, cur = dummynode, head
        
        for i in range(l - 1):
            leftprev, cur = cur, cur.next
        
        prev = None
        for i in range(r-l+1):
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp
        
        leftprev.next.next = cur
        leftprev.next = prev
        
        return dummynode.next
        