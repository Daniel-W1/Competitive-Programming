# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(node, prev):
            if not node:
                return node
            
            if not node.next:
                node.next = prev
                return node
            
            the_next = node.next
            node.next = prev
            
            return reverse(the_next, node)
        
        return reverse(head, None)
        
        