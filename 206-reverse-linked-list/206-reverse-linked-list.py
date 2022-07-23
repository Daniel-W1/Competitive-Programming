# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # this is the first time doing something i already did
        # we are going to do it differently and we are going to analyse the thing.
        if not head:
            return head
        def reverse(node, prev):
            if not node.next:
                node.next = prev
                return node
            the_next = node.next
            node.next = prev
            return reverse(the_next, node)
        return reverse(head, None)
        # time comp O(n)
        # space comp O(n) because of the recursive stack