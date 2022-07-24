# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        cur = head
        while cur:
            if cur in visited:
                return cur
            visited.add(cur)
            cur = cur.next
        return None
    # so the above solution is space O(n) and time O(n)
    # now let's bring the space O(1) sol