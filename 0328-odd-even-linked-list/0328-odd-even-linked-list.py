# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        
        even_head = even_tail = ListNode()
        odd_tail = head
        prev = None
        
        while odd_tail and odd_tail.next:
            the_next = odd_tail.next
            odd_tail.next = odd_tail.next.next
            
            the_next.next = None
            even_tail.next = the_next
            
            
            even_tail = even_tail.next
            prev = odd_tail
            odd_tail = odd_tail.next
        
        if not odd_tail: odd_tail = prev
        odd_tail.next = even_head.next
        
        return head