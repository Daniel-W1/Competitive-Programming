# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, head):
        len = 0
        while head:
            head = head.next
            len += 1
        return len
    def merge(self, head1, head2):
        dummy = tail = ListNode()
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1,tail = head1.next, tail.next
            else:
                tail.next = head2
                head2, tail = head2.next, tail.next
        tail.next = head1 or head2
        return dummy.next
    def split(self, head):
        leng = self.length(head)
        mid = leng//2
        index = 0
        
        current = head
        while index < mid-1:
            current = current.next
            index += 1
        right = current.next
        current.next = None
        return head, right
            
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if self.length(head) < 2:
            return head
        left, right = self.split(head)
        left = self.sortList(left)
        right = self.sortList(right)
        
        res = self.merge(left,right)
        return res