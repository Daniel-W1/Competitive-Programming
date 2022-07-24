# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        answer = {}
        minStack = []
        cur = head
        index = 0
        while cur:
            while minStack and minStack[-1][0].val < cur.val:
                # do something here
                pNode, pIndex = minStack.pop()
                answer[pIndex] = cur.val
                
            minStack.append((cur, index))
            index += 1
            cur = cur.next
        output = [0]*index
        for k in answer:
            output[k] = answer[k]
        return output
            
                
            