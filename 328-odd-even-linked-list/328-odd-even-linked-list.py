# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd = head
        dummy = even = head.next
        cur = head
        while True:
            if odd.next and odd.next.next:
                odd.next = odd.next.next
                odd = odd.next
            if even.next and even.next.next:
                even.next = even.next.next
                even = even.next
            if not odd.next or not even.next:
                break
        even.next = None
        odd.next = dummy
        return head
    
        
            