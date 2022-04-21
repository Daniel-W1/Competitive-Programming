# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
#         arrlist = []
#         current = head
#         while current:
#             arrlist.append(current.val)
#             current = current.next
#         for i, val in enumerate(arrlist):
#             if val < x:
#                 i -= 1
#                 while i >= 0 and arrlist[i] >= x:
#                     arrlist[i], arrlist[i + 1] = arrlist[i+1], arrlist[i]
#                     i -= 1
#         dummy = newnode = ListNode() 
#         for val in arrlist:
#             newnode.next = ListNode(val)
#             newnode = newnode.next
#         return dummy.next
    
        
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        # before and after are the two pointers used to create two list
        # before_head and after_head are used to save the heads of the two lists.
        # All of these are initialized with the dummy nodes created.
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            # If the original list node is lesser than the given x,
            # assign it to the before list.
            if head.val < x:
                before.next = head
                before = before.next
            else:
                # If the original list node is greater or equal to the given x,
                # assign it to the after list.
                after.next = head
                after = after.next

            # move ahead in the original list
            head = head.next

        # Last node of "after" list would also be ending node of the reformed list
        after.next = None
        # Once all the nodes are correctly assigned to the two lists,
        # combine them to form a single list which would be returned.
        before.next = after_head.next

        return before_head.next            
                