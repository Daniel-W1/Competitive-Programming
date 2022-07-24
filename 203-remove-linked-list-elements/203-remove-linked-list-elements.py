# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # dummy = tail = ListNode(0)
        # cur = head
        # while cur:
        #     if cur.val != val: 
        #         tail.next = ListNode(cur.val)
        #         tail = tail.next
        #     cur = cur.next
        # return dummy.next
        # this works but this is not a constant space solution or it creates new listnode 
        # so we need to come up with the constant space solution
        # time O(n)
        # space O(n)
        # i need to come up with the O(1) not done here
        dummy = ListNode(0)
        res = dummy
        
        dummy.next = head
        
        while dummy.next:
            if dummy.next.val == val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
        
        return res.next