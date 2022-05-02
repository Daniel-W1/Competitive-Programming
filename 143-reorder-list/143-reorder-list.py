# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def findmiddle(head):
            slow=head
            fast=head

            while(fast and fast.next):
                slow=slow.next
                fast=fast.next.next
            return slow
        middle = findmiddle(head)
        def reverse(middle):
            if middle is None:
                return middle
            prev = None
            current = middle
            the_next = current.next
            while the_next is not None:
                current.next = prev
                prev = current
                current = the_next
                the_next = the_next.next
            current.next = prev
            return current
        prev = reverse(middle)
        while prev.next:
            nxt = head.next
            head.next = prev
            head = nxt
            
            
            nxt = prev.next
            prev.next = head
            prev = nxt
        
        
        
            
            
            
            
        
            
            
            
        
        

        