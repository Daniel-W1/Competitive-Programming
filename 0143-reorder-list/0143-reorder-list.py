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
        """
            1 --> 2
            
            3 --> 4 --> 5
        
        """
        
        # first let's just find the middle and reverse from there
        slow = fast = head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if not prev: return head
        # cut it in the middle
        prev.next = None
        
        middle = slow
        # reverse from the middle
        prev = None
        while middle:
            the_next = middle.next
            middle.next = prev
            
            prev = middle
            middle = the_next
        
        middle_head = prev
        
        # do the reordering
        current = head
        while current:
            the_next = current.next
            mid_next = middle_head.next
            
            current.next = middle_head
            if the_next:
                middle_head.next = the_next
            
            current = the_next
            middle_head = mid_next
        
        return head
        