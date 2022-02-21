# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        alist = []
        cur = head
        while cur:
            alist.append(cur.val)
            cur = cur.next
        
        for index in range(1, len(alist)):
            value = alist[index]
            pos = index
            
            while pos and alist[pos-1] > value:
                alist[pos] = alist[pos -1]
                pos -=1
            
            alist[pos]= value
        dummy = head = ListNode()
        for i in range(len(alist)):
            head.next = ListNode(alist[i])
            head = head.next
        
            
        
        return dummy.next
        
        
            
    
        