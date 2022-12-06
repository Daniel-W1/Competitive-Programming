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
        
        while odd_tail and odd_tail.next:
            the_next = odd_tail.next
            odd_tail.next = odd_tail.next.next
            
            # print(odd_tail)
            the_next.next = None
            even_tail.next = the_next
            
            
            even_tail = even_tail.next
            odd_tail = odd_tail.next
        
        odd_tail = head
        while odd_tail.next: odd_tail = odd_tail.next
        odd_tail.next = even_head.next
        
        return head