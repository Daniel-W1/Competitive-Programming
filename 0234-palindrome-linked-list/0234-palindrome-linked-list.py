# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        
        current = head
        
        while current:
            stack.append(current)
            current = current.next
        
        
        current = head
        while stack:
            right_node = stack.pop()
            
            if right_node.val != current.val:
                return False
            
            current = current.next
        
        return True