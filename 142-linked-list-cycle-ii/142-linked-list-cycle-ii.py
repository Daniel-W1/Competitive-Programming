# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        slow, fast = head, head
        
        while True:
            slow = slow.next
            if fast and fast.next:
                fast = fast.next.next
            else: return None
            
            if slow == fast:
                break
                
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow