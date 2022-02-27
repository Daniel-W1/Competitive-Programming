# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        if not cur: return cur
        if cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            if cur.next.next:
                self.swapPairs(cur.next.next)
        return cur