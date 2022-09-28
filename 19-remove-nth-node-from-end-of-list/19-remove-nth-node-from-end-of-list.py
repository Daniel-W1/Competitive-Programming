# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev_to_first = None
        first = head
        second = head
        n -= 1
        while n > 0:
            second = second.next
            n -= 1

        while second.next:
            prev_to_first = first
            first = first.next
            second = second.next
        
        # print(first.val)
        if not prev_to_first:
            prev_to_first = first.next
            return prev_to_first
        else:
            prev_to_first.next = prev_to_first.next.next

        return head
        '''
        the most obvious way is to reverse it and then remove the nth node 
        then reverse it back again
        
        
        time O(n) but has 3 passes to reverse, then to remove, then to 
        reverse again
        
        space O(1)
        
        '''
        
#         def reverse(node):
#             prev = None
#             cur = node
#             while cur:
#                 the_next = cur.next
#                 cur.next = prev
#                 cur, prev = the_next, cur
            
#             return prev
        
#         n -= 2
#         new_head = cur = reverse(head)
        
#         if n < 0: 
#             first_node = ListNode()
#             first_node.next = cur.next
#             return reverse(first_node.next)
        
#         while n > 0:
#             cur = cur.next
#             n -= 1
            
#         cur.next = cur.next.next
#         return reverse(new_head)
    
    # but the time and space comp is O(n) and space is O(1)
    
    # now let's try to do it in one pass
    # when ever u want the smart sol using linked lists we need to think of two pointers 
    
    '''
    first = head
    second = head + (k-1) nodes
    keep track of prev to the first node and when u delete delete the first node
    
    '''
    
        
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        