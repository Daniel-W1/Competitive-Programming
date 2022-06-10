# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def findlen(head):
            current = head
            length = 0
            while current:
                length += 1
                current = current.next
            return length
        length = findlen(head)
        if not length or not k%length:
            return head
        position = length - k%length - 1
        current = head
        index = 0
        while index != position:
            current = current.next
            index += 1
        new_head = current.next
        current.next = None
        tail = new_head
        while tail.next:
            tail = tail.next
        tail.next = head
        return new_head