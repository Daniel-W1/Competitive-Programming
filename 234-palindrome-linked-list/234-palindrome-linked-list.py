# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next: return True
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        reverse_prev = None
        while slow:
            temp = slow.next
            slow.next = reverse_prev
            reverse_prev = slow
            slow = temp
        while head and reverse_prev:
            if head.val != reverse_prev.val:
                return False
            head = head.next
            reverse_prev = reverse_prev.next
        return True