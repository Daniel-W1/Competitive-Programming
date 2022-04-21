# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        check = {}
        h1 = head
        while h1:
            if h1.next and h1.val == h1.next.val:
                check[h1.val]= True
            h1 = h1.next
        cur = head
    
        dummy = newnode = ListNode()
        while cur:
            if check.get(cur.val, False):
                cur = cur.next
                if cur == None:
                    newnode.next = None
            else:
                newnode.next = cur
                newnode = newnode.next
                cur = cur.next
                
        return dummy.next
            