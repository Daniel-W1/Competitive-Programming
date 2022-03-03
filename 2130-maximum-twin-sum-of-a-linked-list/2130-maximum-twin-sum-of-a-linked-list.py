# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def find_len(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        
        n = find_len(head)
        cur, index, hash_map = head, 0, {}
        
        while index <= n/2 -1:
            twin = n - index -1
            hash_map[twin] = [cur.val]
            cur = cur.next
            index +=  1

        while index < n:
            hash_map[index].append(cur.val)
            index += 1
            cur = cur.next
        
        return max([sum(val) for val in hash_map.values()])
            
            
            
            