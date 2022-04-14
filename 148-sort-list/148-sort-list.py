# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        arrlist = []
        while current:
            arrlist.append(current.val)
            current = current.next
            
        arrlist = sorted(arrlist)
        if not arrlist:
            return None
        new = ans = ListNode(arrlist[0]) 
        print(type(new))
        for val in arrlist[1:]:
            ans.next = ListNode(val)
            ans = ans.next
        return new
    
        
            
        