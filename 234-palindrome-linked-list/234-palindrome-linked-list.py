# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        org = []
        while cur:
            org.append(cur.val)
            cur = cur.next
        
        fake = head
        def reverse(fake):
            prev = None
            cur = fake
            while cur:
                the_next = cur.next
                cur.next = prev
                prev = cur
                cur = the_next
            return prev
        new = reverse(head)
        rever = []
        while new:
            rever.append(new.val)
            new = new.next
        if rever == org:
            return True
        return False
        
        