# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        the most obvious way is to reverse it and then remove the nth node 
        then reverse it back again
        
        
        time O(n) but has 3 passes to reverse, then to remove, then to 
        reverse again
        
        space O(1)
        
        '''
        
        def reverse(node):
            prev = None
            cur = node
            while cur:
                the_next = cur.next
                cur.next = prev
                cur, prev = the_next, cur
            
            return prev
        
        n -= 2
        new_head = cur = reverse(head)
        
        if n < 0: 
            first_node = ListNode()
            first_node.next = cur.next
            return reverse(first_node.next)
        
        while n > 0:
            cur = cur.next
            n -= 1
            
        cur.next = cur.next.next
        return reverse(new_head)
            
            
        