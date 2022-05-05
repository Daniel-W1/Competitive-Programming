# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def findlength(head):
            l = 0
            cur = head
            while cur:
                l += 1
                cur = cur.next
            return l
        def reverse(head, size):
            prev = None
            current = head
            the_next = current.next
            while size:
                current.next = prev
                prev = current
                current = the_next
                the_next = the_next.next
                size -= 1
            current.next = prev
            return current, the_next
        l = findlength(head)
        times = l//k
        groups = []
        current = head
        for _ in range(times):
            group,next_group = reverse(current, k-1)
            groups.append(group)
            current = next_group
        if next_group:
            groups.append(next_group)
        newhead = first = groups[0]
        while first.next:
            first = first.next
        for g in groups[1:]:
            first.next = g
            first = g
            while first.next:
                first = first.next
        return newhead
            
            
            
                
            
        
        
        
                
                
                
                
                
                
                
                
                
                
                
                
            
            
        
        
            
    
    
    
        