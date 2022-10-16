# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        odds = tail = ListNode()
        cur = head
        prev = None
        while cur:
            if cur.next:
                the_next = cur.next
                prev = cur
                cur.next = cur.next.next
                cur = cur.next
                
                the_next.next = None
                tail.next = the_next
                tail = tail.next
            else:
                break
        
        if cur:
            cur.next = odds.next
        else:
            prev.next = odds.next
            
        return head
                
        