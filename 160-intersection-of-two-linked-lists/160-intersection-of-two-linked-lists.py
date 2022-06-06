# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def length(first):
            leng = 0
            while first:
                leng += 1
                first = first.next
            return leng
        
        l1_len, l2_len = length(headA), length(headB)
        if l1_len > l2_len:
            headA, headB = headB, headA
            
        for _ in range(abs(l1_len-l2_len)):
            headB = headB.next
        
        while headA and headB and headA is not headB:
            headA, headB = headA.next, headB.next
            
        return headA
            
        