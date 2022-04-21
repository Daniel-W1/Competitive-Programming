# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        arrlist = []
        current = head
        while current:
            arrlist.append(current.val)
            current = current.next
        for i, val in enumerate(arrlist):
            if val < x:
                i -= 1
                while i >= 0 and arrlist[i] >= x:
                    arrlist[i], arrlist[i + 1] = arrlist[i+1], arrlist[i]
                    i -= 1
        dummy = newnode = ListNode() 
        for val in arrlist:
            newnode.next = ListNode(val)
            newnode = newnode.next
        return dummy.next
    
        
                    
                